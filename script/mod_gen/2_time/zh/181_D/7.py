def is_8(n):
    for i in range(1,10):
        if n.count(str(i)) == 0:
            continue
        if n.count(str(i)) > 3:
            return False
    return True

if __name__ == '__main__':
    is_8()