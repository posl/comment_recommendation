def main():
    A, B = map(int, input().split())
    def calc(x):
        if x % 2 == 0:
            return x ^ ((x + 1) // 2) % 2
        else:
            return ((x + 1) // 2) % 2
    print(calc(A - 1) ^ calc(B))
