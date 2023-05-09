def main():
    N, M = map(int, input().split())
    a = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        a[A - 1].append(B)
        a[B - 1].append(A)
    for i in range(N):
        a[i].sort()
        print(len(a[i]), *a[i])
