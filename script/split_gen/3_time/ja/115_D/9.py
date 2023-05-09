def main():
    N, X = map(int, input().split())
    # バーガーの層の数
    burger = [1]
    # レベル N バーガーの下から X 層に含まれるパティの枚数
    patties = [0]
    for i in range(N):
        burger.append(burger[i] * 2 + 3)
        patties.append(patties[i] * 2 + 1)
    print(solve(N, X, burger, patties))
