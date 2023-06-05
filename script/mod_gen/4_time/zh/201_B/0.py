def getSecondHeight(height_list):
    if len(height_list) < 2:
        return None
    elif len(height_list) == 2:
        return height_list[0]
    else:
        height_list.sort(reverse=True)
        return height_list[1]

if __name__ == '__main__':
    getSecondHeight()