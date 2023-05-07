def main():
    n = int(input())
    p = list(map(int, input().split()))
    # print(n)
    # print(p)
    ans = 1
    min_p = p[0]
    for i in range(1, n):
        if p[i] <= min_p:
            ans += 1
            min_p = p[i]
    print(ans)

if __name__ == '__main__':
    main()