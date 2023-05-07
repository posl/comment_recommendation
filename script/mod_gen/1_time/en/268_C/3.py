def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == 0 and p[i] == p[i+1] - 1:
            ans += 1
        elif i == n-1 and p[i] == p[i-1] - 1:
            ans += 1
        elif p[i] == p[i-1] - 1 or p[i] == p[i+1] - 1:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()