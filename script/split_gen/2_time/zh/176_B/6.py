def main():
    N, X, T = map(int, input().split())
    num = N // X
    if N % X != 0:
        num += 1
    print(num * T)
