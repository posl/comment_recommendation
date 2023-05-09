def main():
    n = int(input())
    for i in range(0, n + 1):
        for j in range(0, n + 1):
            if 4 * i + 7 * j == n:
                print("Yes")
                return
    print("No")
main()

if __name__ == '__main__':
    main()