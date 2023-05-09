def main():
    #input
    N = int(input())
    As = list(map(int, input().split()))
    mo = 10**9+7
    #compute
    ans = 0
    for i in range(60):
        cnt = 0
        for A in As:
            if A >> i & 1:
                cnt += 1
        ans += (cnt * (N-cnt) * (2**i)) % mo
    #output
    print(ans % mo)
