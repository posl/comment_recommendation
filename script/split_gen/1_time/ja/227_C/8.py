def main():
    # input
    N = int(input())
    # compute
    ans = 0
    for a in range(1,N+1):
        for b in range(a,N//a+1):
            c = N//a//b
            if a*b*c<=N:
                ans += 1
    # output
    print(ans)
