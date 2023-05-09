def main():
    n = int(input())
    ab = [0] * n
    for i in range(n):
        ab[i] = list(map(int, input().split()))
    ab.sort(key=lambda x: x[0])
    ans = 0
    for i in range(n - 1):
        if ab[i][1] >= ab[i + 1][0]:
            ab[i + 1][0] = ab[i][0]
            ab[i + 1][1] = max(ab[i][1], ab[i + 1][1])
        else:
            ans += ab[i][1] - ab[i][0] + 1
    ans += ab[n - 1][1] - ab[n - 1][0] + 1
    print(ans)

if __name__ == '__main__':
    main()