def main():
    N, M, X, T, D = map(int, input().split())
    if M == 0:
        print(T - X * D)
    else:
        print(T)
