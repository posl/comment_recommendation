def main():
    # input
    N = int(input())
    Hs = list(map(int, input().split()))
    # compute
    ans = 1
    for i in range(1, N):
        if Hs[i-1] <= Hs[i]:
            ans += 1
    # output
    print(ans)
