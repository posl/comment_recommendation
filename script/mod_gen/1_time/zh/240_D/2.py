def main():
    N = int(input())
    a = list(map(int, input().split()))
    l = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        l[a[i]] += 1
    ans = 0
    for i in range(2 * 10 ** 5 + 1):
        if l[i] > 0:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()