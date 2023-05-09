def main():
    L = int(input())
    if L <= 3:
        print(L + 1, L)
        for i in range(L):
            print(i + 1, i + 2, 0)
    else:
        print(2 * L, 2 * L)
        for i in range(L - 1):
            print(i + 1, i + 2, 0)
        print(L - 1, L, 0)
        print(L, L + 1, 0)
        for i in range(L):
            print(i + 1, L + i + 1, i)
