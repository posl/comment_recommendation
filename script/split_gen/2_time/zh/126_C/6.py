def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(1,n+1):
        if i >= k:
            ans += 1/n
        else:
            cnt = 0
            while True:
                if i >= k:
                    break
                i *= 2
                cnt += 1
            ans += (1/n)*((1/2)**cnt)
    print(ans)
