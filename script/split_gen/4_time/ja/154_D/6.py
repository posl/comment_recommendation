def main():
    N,K = map(int,input().split())
    P = list(map(int,input().split()))
    ans = 0
    for i in range(K):
        ans += (P[i]+1)/2
    temp = ans
    for i in range(1,N-K+1):
        temp -= (P[i-1]+1)/2
        temp += (P[i+K-1]+1)/2
        if temp > ans:
            ans = temp
    print(ans)
