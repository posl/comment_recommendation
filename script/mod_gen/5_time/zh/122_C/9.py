def solve():
    N, Q = map(int, input().split())
    S = input()
    l = []
    r = []
    for i in range(Q):
        a, b = map(int, input().split())
        l.append(a)
        r.append(b)
    ac = [0] * (N + 1)
    for i in range(N):
        if i == 0:
            continue
        if S[i - 1] == "A" and S[i] == "C":
            ac[i + 1] = ac[i] + 1
        else:
            ac[i + 1] = ac[i]
    for i in range(Q):
        print(ac[r[i]] - ac[l[i]])

if __name__ == '__main__':
    solve()