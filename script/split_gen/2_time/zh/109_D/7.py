def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.append(X)
    x.sort()
    d = [x[i + 1] - x[i] for i in range(N)]
    import math
    ans = math.gcd(*d)
    print(ans)
