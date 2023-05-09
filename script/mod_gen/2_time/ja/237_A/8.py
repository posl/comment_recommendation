def main():
    N = int(input())
    print("Yes" if -2 ** 31 <= N < 2 ** 31 else "No")

if __name__ == '__main__':
    main()