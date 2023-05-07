def main():
    n,k = map(int,input().split())
    ans = 0
    for i in range(n+1):
        tmp = k - i%k
        if tmp > n:
            continue
        else:
            ans += (n - tmp)//k + 1
    print(ans**3)
