def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = [0] * (2 * 10 ** 5 + 1)
    ans = 0
    for i in range(n):
        count[a[i]] += 1
        if count[a[i]] == 1:
            ans += 1
        else:
            ans -= 1
        print(ans)

if __name__ == '__main__':
    main()