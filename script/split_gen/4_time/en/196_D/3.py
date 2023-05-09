def main():
    H, W, A, B = map(int, input().split())
    # H, W, A, B = 4, 4, 8, 0
    # H, W, A, B = 3, 3, 4, 1
    # H, W, A, B = 2, 2, 1, 2
    # H, W, A, B = 1, 1, 0, 1
    # H, W, A, B = 1, 1, 1, 0
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)
    def combination(n, r):
        return factorial(n) // (factorial(n - r) * factorial(r))
    def count(H, W, A, B):
        if H == 1:
            return 1
        else:
            return combination(H + W - 2, H - 1) * count(H - 1, W - A, A, B)
    print(count(H, W, A, B))
