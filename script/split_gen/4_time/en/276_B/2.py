def main():
    N, M = map(int, input().split())
    d = [0] * N
    a = [[] for _ in range(N)]
    for _ in range(M):
        A, B = map(int, input().split())
        A -= 1
        B -= 1
        d[A] += 1
        d[B] += 1
        a[A].append(B)
        a[B].append(A)
    for i in range(N):
        ans = [d[i]]
        ans.extend(sorted(a[i]))
        print(' '.join(map(str, ans)))
