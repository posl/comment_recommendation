def main():
    N,K = map(int,input().split())
    ans = 0
    for i in range(1,N+1):
        ans += (N//i)*(i//K)
    print(ans)
