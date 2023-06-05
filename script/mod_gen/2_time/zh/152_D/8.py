def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = 1
    min = p[0]
    for i in range(1, n):
        if min >= p[i]:
            ans += 1
            min = p[i]
    print(ans)

if __name__ == '__main__':
    main()