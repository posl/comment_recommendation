def main():
    n, x = map(int, input().split())
    cities = list(map(int, input().split()))
    cities.append(x)
    cities.sort()
    diff = [cities[i+1] - cities[i] for i in range(n)]
    gcd = diff[0]
    for i in range(1, n):
        gcd = gcd_cal(gcd, diff[i])
    print(gcd)

if __name__ == '__main__':
    main()