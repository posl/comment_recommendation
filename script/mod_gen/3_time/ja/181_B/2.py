def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    ans = 0
    for i in range(n):
        ans += (b[i] - a[i] + 1) * (a[i] + b[i]) // 2
    print(ans)

if __name__ == '__main__':
    main()