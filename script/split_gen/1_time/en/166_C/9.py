def main():
    #read input
    N,M = map(int,input().split())
    H = list(map(int,input().split()))
    AB = [list(map(int,input().split())) for _ in range(M)]
    #initialize
    ans = N
    #solve
    for a,b in AB:
        if H[a-1] <= H[b-1]:
            ans -= 1
        if H[a-1] >= H[b-1]:
            ans -= 1
    #output
    print(ans)
