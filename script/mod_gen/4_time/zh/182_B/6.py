def main():
    n = int(input())
    a = list(map(int, input().split()))
    max_gcd = 0
    max_n = 0
    for i in range(2, 1001):
        gcd = 0
        for j in range(n):
            if a[j] % i == 0:
                gcd += 1
        if gcd > max_gcd:
            max_gcd = gcd
            max_n = i
    print(max_n)

if __name__ == '__main__':
    main()