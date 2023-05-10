def solve():
    A, B, X = map(int, input().split())
    #print(A, B, X)
    def cost(n):
        return A * n + B * len(str(n))
    def can_buy(n):
        return cost(n) <= X
    def binary_search():
        l = 0
        r = 10 ** 9 + 1
        while r - l > 1:
            m = (l + r) // 2
            if can_buy(m):
                l = m
            else:
                r = m
        return l
    print(binary_search())

if __name__ == '__main__':
    solve()