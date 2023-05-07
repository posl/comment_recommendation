def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = x[1] - x[0]
    for i in range(N):
        d = gcd(d, x[i+1] - x[i])
    print(d)
