def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = [0] * n
    for i in range(n - 1, -1, -1):
        tmp = 0
        for j in range(i + 1, n, i + 1):
            tmp += b[j]
        if tmp % 2 != a[i]:
            b[i] = 1
    ans = []
    for i in range(n):
        if b[i] == 1:
            ans.append(i + 1)
    if len(ans) == 0:
        print(0)
    else:
        print(len(ans))
        print(*ans)

if __name__ == '__main__':
    main()