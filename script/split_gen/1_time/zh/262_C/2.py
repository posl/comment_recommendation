def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i + 1 == a[i]:
            ans += 1
    print(ans)
main()
