def check(X, Y):
    for i in range(X + 1):
        if i * 2 + (X - i) * 4 == Y:
            return True
    return False
X, Y = map(int, input().split())

if __name__ == '__main__':
    check()