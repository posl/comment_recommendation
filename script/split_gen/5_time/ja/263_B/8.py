def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += 1
        if p[i] == 1:
            break
    print(ans)
main()
# 21:20 - 21:29（WA）- 21:35（WA）- 21:38（AC）
