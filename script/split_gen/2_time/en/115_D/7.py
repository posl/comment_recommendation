def solve(N, X):
    burger = [1, 1]
    for i in range(N):
        burger.append(burger[-1] * 2 + 3)
    return eat(N, X, burger)
