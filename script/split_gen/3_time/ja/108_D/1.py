def main():
    L = int(input())
    if L == 2:
        print(4, 5)
        print(1, 2, 0)
        print(2, 3, 0)
        print(3, 4, 0)
        print(1, 3, 1)
        print(2, 4, 1)
    else:
        print(2 * L + 1, 2 * L + 2)
        for i in range(1, L + 1):
            print(i, i + 1, 0)
            print(i, i + L + 1, 1)
        print(L + 1, 2 * L + 2, L)
