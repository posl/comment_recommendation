def main():
    H, W, A, B = map(int, input().split())
    def f(i, j):
        if j == 0:
            return 1
        elif i == 0:
            return 0
        else:
            return f(i - 1, j) + f(i - 1, j - 1)
    def g(i, j):
        if i == 0:
            return 1
        elif j == 0:
            return 0
        else:
            return g(i - 1, j) + g(i - 1, j - 1)
    ans = 0
    for i in range(H - A):
        ans += f(A, i) * g(B, W - A - i)
    print(ans)

if __name__ == '__main__':
    main()