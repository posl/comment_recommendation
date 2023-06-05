def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    ans += n * sum([i ** 2 for i in a])
    ans -= sum(a) ** 2
    print(ans)

if __name__ == '__main__':
    main()