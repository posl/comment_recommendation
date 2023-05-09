def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    A.reverse()
    print(sum([max(a - (i // K) * X, 0) for i, a in enumerate(A)]))
