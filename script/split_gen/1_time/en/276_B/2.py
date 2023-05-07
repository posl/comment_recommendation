def main():
    N, M = map(int, input().split())
    a = [[] for i in range(N)]
    for i in range(M):
        A, B = map(int, input().split())
        a[A - 1].append(B)
        a[B - 1].append(A)
    for i in range(N):
        a[i] = sorted(a[i])
        print(len(a[i]), end = ' ')
        for j in range(len(a[i])):
            print(a[i][j], end = ' ')
        print('')
