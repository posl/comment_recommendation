def main():
    H, W = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(H)]
    a = []
    b = []
    c = []
    d = []
    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 0:
                a.append(A[i][j])
            else:
                b.append(A[i][j])
    for i in range(H):
        for j in range(W):
            if (i + j) % 2 == 0:
                c.append(A[i][j])
            else:
                d.append(A[i][j])
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    if a == c and b == d:
        print('Yes')
    else:
        print('No')
