def main():
    N, M = map(int, input().split())
    if M == 1:
        for i in range(N):
            for j in range(N):
                print(abs(i - j), end=" ")
            print()
    elif M == 2:
        for i in range(N):
            for j in range(N):
                print(min(i + j, 2 * N - i - j - 2), end=" ")
            print()
    elif M == 3:
        for i in range(N):
            for j in range(N):
                print(min(i + j, 2 * N - i - j - 2, i + N - j - 1, j + N - i - 1), end=" ")
            print()
    else:
        print(-1)
