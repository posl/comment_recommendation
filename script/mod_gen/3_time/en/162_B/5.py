def main():
    N = int(input())
    print((N // 3) * (1 + N // 3) * 3 // 2 + (N // 5) * (1 + N // 5) * 5 // 2 - (N // 15) * (1 + N // 15) * 15 // 2)

if __name__ == '__main__':
    main()