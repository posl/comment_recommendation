def main():
    n = int(input())
    a = [int(i) for i in input().split()]
    angle = 360 / n
    ans = 0
    for i in range(n):
        ans = max(ans, sum(a[i:]) + sum(a[:i]) + angle * (n - 1))
    print(int(360 - ans))

if __name__ == '__main__':
    main()