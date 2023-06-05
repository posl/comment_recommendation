def main():
    N, X, Y = map(int, input().split())
    result = 0
    for i in range(N-1, 0, -1):
        if i >= X:
            result += 1
        else:
            result += 1 + (X - i) * (N - i - 1)
    print(result)
