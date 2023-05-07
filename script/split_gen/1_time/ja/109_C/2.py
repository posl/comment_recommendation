def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = abs(x[0] - x[1])
    for i in range(1, N + 1):
        d = gcd(d, abs(x[i] - x[i + 1]))
    print(d)
