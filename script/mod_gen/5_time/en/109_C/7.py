def main():
    n,x = map(int,input().split())
    cities = list(map(int,input().split()))
    cities.append(x)
    cities.sort()
    diff = []
    for i in range(1,n+1):
        diff.append(cities[i]-cities[i-1])
    gcd = diff[0]
    for i in range(1,n):
        gcd = euclid(gcd,diff[i])
    print(gcd)

if __name__ == '__main__':
    main()