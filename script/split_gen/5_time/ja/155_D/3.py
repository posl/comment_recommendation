def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    a.reverse()
    ans = 1
    for i in range(k):
        ans *= a[i]
    print(ans)
main()
