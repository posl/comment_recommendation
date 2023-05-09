def main():
    n = int(input())
    for i in range(1, 2 * n + 1):
        print(i)
        if int(input()) == 0:
            return

if __name__ == '__main__':
    main()