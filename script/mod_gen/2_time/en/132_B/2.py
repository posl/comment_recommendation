def main():
    n = int(input())
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(1, n - 1):
        if p[i - 1] < p[i] < p[i + 1] or p[i + 1] < p[i] < p[i - 1]:
            ans += 1
    print(ans)
main()

if __name__ == '__main__':
    main()