def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    max_gcd = 0
    for k in range(2,1001):
        gcd = 0
        for i in range(n):
            if a[i] % k == 0:
                gcd += 1
        if max_gcd < gcd:
            max_gcd = gcd
            k_max_gcd = k
    print(k_max_gcd)

if __name__ == '__main__':
    main()