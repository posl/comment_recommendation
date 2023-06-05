def check(X, Y):
    for i in range(0, X+1):
        for j in range(0, X+1):
            if i + j == X and i*2 + j*4 == Y:
                return True
    return False
X, Y = map(int, input().split())
