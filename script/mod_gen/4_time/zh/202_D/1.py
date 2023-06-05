def count(a,b):
    if a == 0 or b == 0:
        return 1
    else:
        return count(a-1,b) + count(a,b-1)

if __name__ == '__main__':
    count()