def findIntegers():
    A, B = map(int, input().split())
    if A > B:
        print(0)
    else:
        print(B - A + 1)
findIntegers()

if __name__ == '__main__':
    findIntegers()