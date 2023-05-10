def main():
    n = int(input())
    a = list(map(int, input().split()))
    x = int(input())
    sum_a = sum(a)
    loop = x // sum_a
    ans = loop * n
    x -= loop * sum_a
    for i in range(n):
        if x < 0:
            break
        x -= a[i]
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()