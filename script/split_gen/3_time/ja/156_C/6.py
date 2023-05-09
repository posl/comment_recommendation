def main():
    N = int(input())
    X = [int(x) for x in input().split()]
    X.sort()
    if N % 2 == 0:
        print(X[N//2] - X[N//2-1])
    else:
        print(0)
