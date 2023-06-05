def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = a[0]
    for i in range(1, n):
        ans = ans if ans == 1 else gcd(ans, a[i])
    print(ans)

if __name__ == '__main__':
    main()