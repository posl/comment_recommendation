def main():
    N, X = map(int, input().split())
    burger = [1, 1]
    for n in range(2, N + 1):
        burger.append(burger[n - 1] * 2 + 3)
    print(solve(N, X, burger))

if __name__ == '__main__':
    main()