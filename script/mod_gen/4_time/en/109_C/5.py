def solve():
    n, x = map(int, input().split())
    cities = list(map(int, input().split()))
    cities.append(x)
    cities.sort()
    distances = []
    for i in range(n):
        distances.append(cities[i+1] - cities[i])
    result = distances[0]
    for i in range(1, n):
        result = gcd(result, distances[i])
    print(result)

if __name__ == '__main__':
    solve()