def main():
    N = int(input())
    print(N // 100 + 1 if N % 100 != 0 else N // 100)

if __name__ == '__main__':
    main()