def main():
    N = int(input())
    for i in range(N // 4 + 1):
        if (N - 4 * i) % 7 == 0:
            print("Yes")
            return
    print("No")
main()

if __name__ == '__main__':
    main()