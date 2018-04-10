"""
@author Anurag Regmi
@github anuragregmi
"""
import json


def _images_dict():
    """
    Load contents of images.json

    :return: dictionary containing images data
    """
    import os

    store_path = os.path.dirname(os.path.abspath(__file__))
    image_list_file = "/images.json"
    images_location = "{}{}".format(store_path, image_list_file)
    images = dict()
    with open(images_location, 'r') as file:
        images.update(json.load(file))
    return images


class Image:
    """
    Represents an image

    Attributes

    `root`: root url of the image storage
    `folder`: folder name

    `name`: image filename
    `url`: url where image exists


    Methods

    `all`:
        list all images as image object

    Usage:
        images = Image.all() # all images
        # print image name and and url
        for image in images:
            print(image.name)
            print(image.url)


    """
    __image_dict = _images_dict()
    root = __image_dict.get('root_url')
    folder_id = __image_dict.get('folder')
    thumbnail_folder = __image_dict.get('thumbnail_folder')

    def __init__(self, name):
        self.name = name
        self.url = '{}{}{}.jpg'.format(self.root, self.folder_id, self.name)
        self.thumbnail = '{}{}{}{}.png'.format(self.root, self.folder_id,
                                               self.thumbnail_folder, self.name)

    @classmethod
    def all(cls):
        """
        list all images
        :return: list of Image objects which are available
        """
        images = list()
        for name in cls.__image_dict.get('files'):
            images.append(cls(name))
        return images
