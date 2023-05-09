def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    # b = [a[i] * (i + 1) for i in range(n)]
    # print(b)
    # c = [a[i] * (n - i) for i in range(n)]
    # print(c)
    # sum_b = [0]
    # sum_c = [0]
    # for i in range(n):
    #     sum_b.append(sum_b[i] + b[i])
    #     sum_c.append(sum_c[i] + c[i])
    # print(sum_b)
    # print(sum_c)
    # ans = 0
    # for i in range(n - m + 1):
    #     ans = max(ans, sum_c[i] + sum_b[i + m] - sum_b[i] - sum_c[i + m])
    # print(ans)
    sum_b = [0]
    sum_c = [0]
    for i in range(n):
        sum_b.append(sum_b[i] + a[i] * (i + 1))
        sum_c.append(sum_c[i] + a[i] * (n - i))
    # print(sum_b)
    # print(sum_c)
    ans = 0
    for i in range(n - m + 1):
        ans = max(ans, sum_c[i] + sum_b[i + m] - sum_b[i] - sum_c[i + m])
    print(ans)

if __name__ == '__main__':
    main()