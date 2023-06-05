def main():
    N, M = map(int, input().split())
    if N == 1:
        print(0)
        return
    if M == 1:
        for i in range(N):
            for j in range(N):
                print(max(i, j), end=' ')
            print()
        return
    if M == 2:
        for i in range(N):
            for j in range(N):
                print(max(i, j) + min(N - 1 - i, N - 1 - j), end=' ')
            print()
        return
    if M == 3:
        for i in range(N):
            for j in range(N):
                print(max(i, j) + (N - 1 - min(i, j)), end=' ')
            print()
        return
    if M == 4:
        for i in range(N):
            for j in range(N):
                print(max(i, j) + min(i, j), end=' ')
            print()
        return
    if M == 5:
        for i in range(N):
            for j in range(N):
                print(max(i, j) + max(N - 1 - i, N - 1 - j), end=' ')
            print()
        return
    if M == 6:
        for i in range(N):
            for j in range(N):
                print(max(i, j) + (N - 1 - max(i, j)), end=' ')
            print()
        return
    if M == 7:
        for i in range(N):
            for j in range(N):
                print(max(i, j) + (min(i, j)), end=' ')
            print()
        return
    if M == 8:
        for i in range(N):
            for j in range(N):
                print(max(i, j) + min(N - 1 - i, N - 1 - j), end=' ')
            print()
        return
    if M == 9:
        for i in range(N):
            for j in range(N):
                print(max(i, j) + (N - 1 - max(i, j)), end=' ')
            print()
        return
    if M == 10:
        for i in range(N):
            for j in range(N):
                print(max(i, j) + min(i, j), end=' ')
            print()
