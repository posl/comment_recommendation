def check(x):
    if x == 0:
        return True
    if x < 0:
        return False
    for i in range(N):
        if check(x - A[i]) or check(x - B[i]):
            return True
    return False
N, X = map(int, input().split())
A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

if __name__ == '__main__':
    check()