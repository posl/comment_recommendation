def solve():
    N,Q = map(int,input().split())
    S = input()
    l = [0]*N
    for i in range(N-1):
        if S[i:i+2] == 'AC':
            l[i] = 1
    for i in range(N-1):
        l[i+1] += l[i]
    for _ in range(Q):
        l_i,r_i = map(int,input().split())
        print(l[r_i-2]-l[l_i-1])
solve()
