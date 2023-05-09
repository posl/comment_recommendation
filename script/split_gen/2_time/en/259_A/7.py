def main():
    N, M, X, T, D = map(int, input().split())
    result = T
    if M < X:
        result += (X - M) * D
    elif M > X:
        result += (N - M) * D
    print(result)
