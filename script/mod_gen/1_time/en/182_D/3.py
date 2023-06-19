def main():
    n = int(input())
    a = list(map(int, input().split()))
    if sum(a) <= 0:
        print(0)
        return
    ans = 0
    for i in range(n):
        ans += a[i]
        if ans < 0:
            print(0)
            return
    print(ans)
main()
