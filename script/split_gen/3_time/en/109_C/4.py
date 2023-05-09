def main():
    n, x = map(int, input().split())
    cities = list(map(int, input().split()))
    cities.append(x)
    cities.sort()
    distances = []
    for i in range(n):
        distances.append(cities[i+1] - cities[i])
    gcd = distances[0]
    for i in range(n-1):
        gcd = calc_gcd(gcd, distances[i+1])
    print(gcd)
