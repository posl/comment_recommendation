def main():
    n, x = map(int, input().split())
    city = list(map(int, input().split()))
    city.append(x)
    city.sort()
    city_dis = []
    for i in range(n):
        city_dis.append(city[i+1] - city[i])
    gcd = city_dis[0]
    for i in range(n-1):
        gcd = gcd_cal(gcd, city_dis[i+1])
    print(gcd)
    return 0

if __name__ == '__main__':
    main()