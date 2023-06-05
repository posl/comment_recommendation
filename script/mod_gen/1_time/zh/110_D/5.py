def main():
    n,m = map(int,input().split())
    i = 2
    ans = 1
    while i*i <= m:
        cnt = 0
        while m % i == 0:
            cnt += 1
            m //= i
        ans *= cnt + 1
        i += 1
    if m > 1:
        ans *= 2
    print(ans)
main()
