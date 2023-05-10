def main():
    N, X = map(int, input().split())
    patty = [1]
    bread = [1]
    for i in range(50):
        patty.append(patty[i] * 2 + 1)
        bread.append(bread[i] * 2 + 3)
    def f(N, X):
        if N == 0:
            return 0 if X <= 0 else 1
        elif X <= 1 + bread[N - 1]:
            return f(N - 1, X - 1)
        else:
            return patty[N - 1] + 1 + f(N - 1, X - 2 - bread[N - 1])
    print(f(N, X))
