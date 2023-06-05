def solve():
    N, Q = map(int, input().split())
    S = input()
    l = [0] * N
    for i in range(1, N):
        l[i] = l[i-1]
        if S[i-1] == "A" and S[i] == "C":
            l[i] += 1
    for i in range(Q):
        l_i, r_i = map(int, input().split())
        print(l[r_i-1]-l[l_i-1])
solve()
