def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    a_sum = sum(a)
    k = x // a_sum
    ans = n * k
    x -= a_sum * k
    i = 0
    while x > 0:
        x -= a[i]
        ans += 1
        i += 1
    print(ans)

if __name__ == '__main__':
    main()