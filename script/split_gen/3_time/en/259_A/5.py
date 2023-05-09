def main():
    N, M, X, T, D = map(int, input().split())
    if M < X:
        height = T + (M * D)
    else:
        height = T + ((X - 1) * D)
    print(height)
