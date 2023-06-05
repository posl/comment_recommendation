def main():
    N = int(input())
    if N % 4 == 0 or N % 7 == 0 or N % 11 == 0:
        print("Yes")
        return
    for i in range(1, N // 4 + 1):
        for j in range(1, N // 7 + 1):
            if 4 * i + 7 * j == N:
                print("Yes")
                return
    print("No")

if __name__ == '__main__':
    main()