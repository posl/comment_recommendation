def gcd(a,b):
    if a%b == 0:
        return b
    else:
        return gcd(b,a%b)
n,x = map(int,input().split())
cities = list(map(int,input().split()))
cities.append(x)
cities.sort()
#print(cities)

if __name__ == '__main__':
    gcd()