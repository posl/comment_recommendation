def main():
    N, M = map(int, input().split())
    if N == 1:
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                print(0)
    elif N == 2:
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    print(0, end=' ')
                else:
                    print(1, end=' ')
            print()
    else:
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if i == j:
                    print(0, end=' ')
                elif i == 1 or j == 1:
                    print(1, end=' ')
                else:
                    print(2, end=' ')
            print()
