def solve():
    N,A,B,C = map(int,input().split())
    l = [int(input()) for _ in range(N)]
    INF = 10**9
    ans = INF
    for i in range(4**N):
        mp = 0
        a,b,c = 0,0,0
        for j in range(N):
            if (i >> (2*j)) & 3 == 0:
                continue
            elif (i >> (2*j)) & 3 == 1:
                mp += 10
                a += l[j]
            elif (i >> (2*j)) & 3 == 2:
                mp += 10
                b += l[j]
            elif (i >> (2*j)) & 3 == 3:
                mp += 10
                c += l[j]
        if min(a,b,c) > 0:
            ans = min(ans,mp+abs(A-a)+abs(B-b)+abs(C-c))
    print(ans)

if __name__ == '__main__':
    solve()