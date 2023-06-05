def check(a, b):
    for i in range(a+1):
        for j in range(a+1):
            if i * 2 + j * 4 == b:
                return True
    return False
a, b = map(int, input().split())

if __name__ == '__main__':
    check()