def main():
    n = int(input())
    x = list(map(int, input().split()))
    ans = 10**10
    for i in range(min(x), max(x) + 1):
        ans = min(ans, sum([(j - i) ** 2 for j in x]))
    print(ans)

if __name__ == '__main__':
    main()