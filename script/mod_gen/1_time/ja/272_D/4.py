def main():
    N, M = map(int, input().split())
    if N == 1:
        print(0)
        return
    if M == 1:
        for i in range(N):
            for j in range(N):
                print(abs(i - j), end=' ')
            print()
        return
    if M == 2:
        for i in range(N):
            for j in range(N):
                print(abs(i - j) + 1, end=' ')
            print()
        return
    if M == 3:
        for i in range(N):
            for j in range(N):
                print(abs(i - j) + 2, end=' ')
            print()
        return
    if M == 4:
        for i in range(N):
            for j in range(N):
                print(abs(i - j) + 3, end=' ')
            print()
        return
    if M == 5:
        for i in range(N):
            for j in range(N):
                print(abs(i - j) + 4, end=' ')
            print()
        return
    if M == 6:
        for i in range(N):
            for j in range(N):
                print(abs(i - j) + 5, end=' ')
            print()
        return
    if M == 7:
        for i in range(N):
            for j in range(N):
                print(abs(i - j) + 6, end=' ')
            print()
        return
    if M == 8:
        for i in range(N):
            for j in range(N):
                print(abs(i - j) + 7, end=' ')
            print()
        return
    if M == 9:
        for i in range(N):
            for j in range(N):
                print(abs(i - j) + 8, end=' ')
            print()
        return
    if M == 10:
        for i in range(N):
            for j in range(N):
                print(abs(i - j) + 9, end=' ')
            print()
        return
    if M == 11:
        for i in range(N):
            for j in range(N):
                print(abs(i - j) + 10, end=' ')
            print()
        return
    if M == 12:
        for i in range(N):
            for j in range(N):
                print(abs

if __name__ == '__main__':
    main()