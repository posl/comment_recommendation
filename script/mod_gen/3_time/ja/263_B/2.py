def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        ans += 1
        if p[i] == n:
            break
        else:
            n = p[i]
    print(ans)

if __name__ == '__main__':
    main()