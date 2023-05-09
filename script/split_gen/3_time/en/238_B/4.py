def main():
    N = int(input())
    A = list(map(int, input().split()))
    X = 360
    for i in range(N):
        X = min(X, abs(X-A[i]))
    print(X)
