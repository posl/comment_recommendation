def main():
    N = int(input())
    for i in range(0, 26):
        for j in range(0, 15):
            if (4 * i) + (7 * j) == N:
                print("Yes")
                return
    print("No")
    return

if __name__ == '__main__':
    main()