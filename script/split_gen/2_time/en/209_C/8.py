def main():
    #input
    N = int(input())
    Cs = list(map(int, input().split()))
    MOD = 10**9+7
    #compute
    if Cs[0] == 1:
        ans = 1
    else:
        ans = 0
    for i in range(1, N):
        ans *= Cs[i-1]-Cs[i]+1
        ans %= MOD
        if Cs[i] < Cs[i-1]:
            ans *= pow(Cs[i-1]-Cs[i]+1, MOD-2, MOD)
            ans %= MOD
        elif Cs[i] > Cs[i-1]+1:
            ans = 0
            break
    #output
    print(ans)
