def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        ans += 1
        if p[i] == n:
            break
    print(ans)

if __name__ == '__main__':
    main()