def rotate(image):
    image = zip(*image[::-1])
    return image

if __name__ == '__main__':
    rotate()