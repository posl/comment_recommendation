def printDoublePages(pages):
    if pages % 2 == 0:
        return pages / 2
    else:
        return pages / 2 + 1

if __name__ == '__main__':
    printDoublePages()