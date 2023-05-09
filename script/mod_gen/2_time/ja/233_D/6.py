def main():
    N,K = map(int,input().split())
    A = list(map(int,input().split()))
    #累積和
    Sum = [0]
    for i in range(N):
        Sum.append(Sum[i]+A[i])
    #累積和の差がKになる組み合わせを数える
    from collections import Counter
    c = Counter(Sum)
    ans = 0
    for i in c:
        if i + K in c:
            ans += c[i] * c[i+K]
    print(ans)

if __name__ == '__main__':
    main()