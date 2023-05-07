def main():
    N, X = map(int, input().split())
    burger = [0] * (N + 1)
    burger[0] = 1
    for i in range(1, N + 1):
        burger[i] = burger[i - 1] * 2 + 3
    def eat_burger(N, X):
        if N == 0:
            return 0
        elif X == 1:
            return 0
        elif X <= burger[N - 1] + 1:
            return eat_burger(N - 1, X - 1)
        elif X == burger[N - 1] + 2:
            return burger[N - 1] + 1
        elif X <= 2 * burger[N - 1] + 2:
            return burger[N - 1] + 1 + eat_burger(N - 1, X - burger[N - 1] - 2)
        else:
            return burger[N]
    print(eat_burger(N, X))
