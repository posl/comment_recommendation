def main():
    N, M = input().split()
    N = int(N)
    M = int(M)
    a = [0] * N
    b = [0] * N
    for i in range(M):
        a[i], b[i] = input().split()
        a[i] = int(a[i])
        b[i] = int(b[i])
    for i in range(N):
        c = 0
        for j in range(M):
            if a[j] == i + 1:
                c += 1
            elif b[j] == i + 1:
                c += 1
        print(c)
