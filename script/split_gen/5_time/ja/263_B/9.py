def main():
    n = int(input())
    p = list(map(int, input().split()))
    print(p)
    ans = 0
    for i in range(1, n):
        if p[i-1] == n:
            ans = i
            break
    print(ans)
main()
