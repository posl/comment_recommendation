def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if p[i] == n:
            ans += 1
        else:
            ans = 0
    print(ans)

if __name__ == '__main__':
    main()