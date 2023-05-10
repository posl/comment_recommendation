def rotate(image):
    image = zip(*image[::-1])
    return image
