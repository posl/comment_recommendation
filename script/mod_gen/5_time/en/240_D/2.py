def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = [0] * (2 * 10**5 + 1)
    for i in range(n):
        l[a[i]] += 1
    ans = 0
    for i in range(2 * 10**5):
        ans = max(ans, l[i] + l[i + 1] + l[i + 2])
    print(ans)

if __name__ == '__main__':
    main()