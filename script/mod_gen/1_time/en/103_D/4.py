def main():
    N, M = map(int, input().split())
    a = []
    b = []
    for i in range(M):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    ans = 0
    for i in range(M):
        if i == 0:
            if a[i] > 1:
                ans += 1
        if i == M-1:
            if b[i] < N:
                ans += 1
        if i != 0 and i != M-1:
            if (a[i] - b[i-1]) > 1:
                ans += 1
    print(ans)
main()
