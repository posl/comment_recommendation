def main():
    n,k = map(int,input().split())
    if k <= n:
        print(1/2)
    else:
        ans = 0
        for i in range(1,n+1):
            if i >= k:
                ans += 1/n
            else:
                x = 1
                while i * x < k:
                    x *= 2
                ans += (1/2)**x
        print(ans/n)
