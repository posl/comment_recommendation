def is_polygon(n, list):
    list.sort()
    if list[n-1] < sum(list[0:n-1]):
        return True
    return False

if __name__ == '__main__':
    is_polygon()