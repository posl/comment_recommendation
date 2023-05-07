def main():
    N, X = map(int, input().split())
    x = list(map(int, input().split()))
    x.sort()
    # print(x)
    # print(x[-1])
    # print(x[0])
    # print(x[-1] - x[0])
    # print(x[-1] - x[0])
    D = x[-1] - x[0]
    for i in range(1, N):
        # print(x[-1] - x[i])
        # print(x[i] - x[0])
        D = min(D, x[-1] - x[i], x[i] - x[0])
        # print(D)
    # print(D)
    print(D)
