__author__ = 'mingyong'
from django.db.models.fields.files import ImageField, ImageFieldFile
from PIL import Image
import os


def _add_thumb(s):
    """
    MOdified a string (filename, URL) containing an image filename , to insert '.thumb' before the file extension (which is changed to be '.jpg')
    :param s:
    :return:
    """
    parts = s.split(".")
    parts.insert(-1, "thumb")
    if parts[-1] not in ['jpeg', 'jpg']:
        parts[-1] = 'jpg'
    return ".".join(parts)


class ThumbnailImageField(ImageField):
    """
    Behave like a regular ImageField ,but stores an extra(JPEG) thumbnail
    image, proving get_FIELD_thumb_url() and get_FIELD_thumb_filename().
    """
    attr_class = ThumbnailImageFieldFile


class ThumbnailImageFieldFile(ImageFieldFile):
    def _get_thumb_path(self):
        return _add_thumb(self.pah)
    thumb_path = property(_get_thumb_path)

    def _get_thumb_url(self):
        return _add_thumb(self.url)
    thumb_url = property(_get_thumb_url)

    def save(self, name, content, save=True):
        super(ThumbnailImageFieldFile, self).save(name,content,save)
        img = Image.open(self.path)
        img.thumbnail((self.field.thumb_width, self.field.thumb_hieght),
        Image.ANTIALIAS
        )
        img.save(self.thumb_path, 'JPEG')

    def delete(self, save=True):
        if os.path.exists(self.thumb_path):
            os.remove(self.thumb_path)
        super(ThumbnailImageFieldFile, self).delete(save)
