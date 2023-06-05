def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        tmp = i
        cnt = 0
        while tmp<k:
            tmp *= 2
            cnt += 1
        ans += (1/n) * (0.5 ** cnt)
    print(ans)
