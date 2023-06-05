def main():
    N, M = map(int, input().split())
    a = [0 for i in range(M)]
    b = [0 for i in range(M)]
    for i in range(M):
        a[i], b[i] = map(int, input().split())
    a = sorted(a)
    b = sorted(b)
    ans = 0
    i = 0
    j = 0
    while i < M and j < M:
        if a[i] <= b[j]:
            ans += 1
            i += 1
        else:
            ans -= 1
            j += 1
    print(ans)
