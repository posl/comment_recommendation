def main():
    n, m, k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    #累積和
    a_acc = [0]
    b_acc = [0]
    for i in range(n):
        a_acc.append(a_acc[i] + a[i])
    for i in range(m):
        b_acc.append(b_acc[i] + b[i])
    ans = 0
    j = m
    for i in range(n + 1):
        if a_acc[i] > k:
            break
        while b_acc[j] > k - a_acc[i]:
            j -= 1
        ans = max(ans, i + j)
    print(ans)

if __name__ == '__main__':
    main()