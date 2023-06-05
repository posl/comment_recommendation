def main():
    n = int(input())
    a = list(map(int, input().split()))
    mod = 10**9 + 7
    sum = 0
    for i in range(n):
        sum += a[i] * (sum(a) - a[i])
    print(sum % mod)
main()
