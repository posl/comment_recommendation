def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == n:
            ans = 1
        else:
            ans += 1
    print(ans)
main()
