def solve():
    N, K = map(int, input().split())
    P = list(map(int, input().split()))
    C = list(map(int, input().split()))
    P = [x - 1 for x in P]
    ans = -10 ** 18
    for i in range(N):
        j = P[i]
        s = []
        while j != i:
            s.append(C[j])
            j = P[j]
        s.append(C[i])
        t = [0]
        for x in s:
            t.append(t[-1] + x)
        for k in range(1, len(t)):
            if k > K:
                break
            if t[k] > 0:
                tmp = t[k] * ((K - k) // len(s))
                if tmp > ans:
                    ans = tmp
            if t[k] + t[-1] > ans:
                ans = t[k] + t[-1]
    print(ans)
solve()

if __name__ == '__main__':
    solve()