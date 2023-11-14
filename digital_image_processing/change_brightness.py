from PIL import Image


def change_brightness(img: Image, level: float) -> Image:
    """
    Change the brightness of a PIL Image to a given level
    :param img: a PIL Image
    :param level: the given level of brightness
    :return: the Image with given level of brightness
    """

    def brightness(c: int) -> float:
        return 128 + level + (c - 128)

    if not -255.0 <= level <= 255.0:
        raise ValueError("Level must between -255.0 (black) and 255.0 (white)!")

    return img.point(brightness)
