def main():
    L = int(input())
    if L == 2:
        print(4, 4)
        print(1, 2, 0)
        print(2, 3, 0)
        print(3, 4, 0)
        print(1, 4, 1)
    else:
        print(2 * L, 2 * L)
        for i in range(L):
            print(1, i + 2, i)
            print(i + 2, L + i + 2, 0)
        print(1, L + 1, L - 1)
