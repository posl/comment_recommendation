def main():
    N, X, T = map(int, input().split())
    if N % X == 0:
        ans = int(N / X) * T
    else:
        ans = (int(N / X) + 1) * T
    print(ans)
