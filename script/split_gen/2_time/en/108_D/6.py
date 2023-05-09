def main():
    L = int(input())
    if L % 2 == 0:
        print(2 * L // 2 + 1, 2 * L)
        for i in range(1, L // 2 + 1):
            print(i, i + 1, 0)
            print(i, i + L // 2 + 1, 1)
        print(L // 2 + 1, 2 * L, 0)
    else:
        print(2 * L // 2 + 2, 2 * L + 1)
        for i in range(1, L // 2 + 1):
            print(i, i + 1, 0)
            print(i, i + L // 2 + 2, 1)
        print(L // 2 + 1, L // 2 + 2, 0)
        print(L // 2 + 2, 2 * L + 1, 1)
