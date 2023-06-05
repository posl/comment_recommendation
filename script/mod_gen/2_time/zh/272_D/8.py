def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.reverse()
    for i in range(n):
        for j in range(i+1,n):
            if (a[i]+a[j])%2 == 0:
                print(a[i]+a[j])
                return
    print(-1)
main()
