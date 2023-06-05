def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]*n
    for i in range(n):
        if a[i] > n:
            print(-1)
            return
        b[a[i]-1] += 1
    for i in range(n):
        if b[i] > 1:
            print(-1)
            return
    ans = 0
    for i in range(n):
        if a[i] != i+1:
            ans += 1
    print(ans)
main()
