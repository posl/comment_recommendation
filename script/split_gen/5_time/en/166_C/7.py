def main():
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    AB = [list(map(int,input().split())) for _ in range(M)]
    #print(N,M,H,AB)
    #print(N,M,H)
    #print(AB)
    #print()
    ans = N
    for ab in AB:
        if H[ab[0]-1] <= H[ab[1]-1]:
            ans -= 1
        if H[ab[0]-1] >= H[ab[1]-1]:
            ans -= 1
    print(ans)
