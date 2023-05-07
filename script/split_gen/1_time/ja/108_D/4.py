def main():
    L = int(input())
    print(2 * L + 2, 2 * L + 1)
    for i in range(L + 1):
        print(i + 1, i + 2, 0)
    for i in range(L):
        print(i + 1, i + 2, 1)
    print(L + 1, L + 2, 0)
