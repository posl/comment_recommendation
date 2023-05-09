def rotate(n):
    n = n[::-1]
    n = n.replace('0', 'a')
    n = n.replace('1', 'b')
    n = n.replace('6', 'c')
    n = n.replace('8', 'd')
    n = n.replace('9', 'e')
    n = n.replace('a', '0')
    n = n.replace('b', '1')
    n = n.replace('c', '9')
    n = n.replace('d', '8')
    n = n.replace('e', '6')
    return n

if __name__ == '__main__':
    rotate()