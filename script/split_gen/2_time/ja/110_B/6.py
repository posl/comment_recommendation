def main():
    N, M, X, Y = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    x.sort()
    y.sort()
    if X < y[0] <= Y and x[-1] < y[0]:
        print("No War")
    else:
        print("War")
