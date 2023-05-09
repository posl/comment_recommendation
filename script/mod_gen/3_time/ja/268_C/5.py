def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if i == p[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()