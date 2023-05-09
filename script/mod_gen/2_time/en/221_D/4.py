def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    # 累積和
    # 1日目から10^9日目までのログイン人数
    c = [0] * (10**9+1)
    for i in range(n):
        c[a[i]] += 1
        c[a[i]+b[i]] -= 1
    for i in range(1, 10**9+1):
        c[i] += c[i-1]
    # 1人からn人までのログイン人数
    d = [0] * (n+1)
    for i in range(1, 10**9+1):
        d[c[i]] += 1
    # 累積和
    for i in range(1, n+1):
        d[i] += d[i-1]
    for i in range(1, n+1):
        print(d[i]-d[i-1])
main()

if __name__ == '__main__':
    main()