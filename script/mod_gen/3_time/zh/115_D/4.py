def func():
    n, x = map(int, input().split())
    buns = [1]
    patties = [1]
    for i in range(n):
        buns.append(2 * buns[-1] + 3)
        patties.append(2 * patties[-1] + 1)
    def dfs(n, x):
        if n == 0:
            return 0 if x <= 0 else 1
        elif x <= 1 + buns[n - 1]:
            return dfs(n - 1, x - 1)
        else:
            return patties[n - 1] + 1 + dfs(n - 1, x - 2 - buns[n - 1])
    print(dfs(n, x))

if __name__ == '__main__':
    func()