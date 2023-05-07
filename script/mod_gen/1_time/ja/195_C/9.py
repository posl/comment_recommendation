def main():
    N = int(input())
    print(N - 999 + (N - 1000) // 3 + 1 if N > 1000 else N)

if __name__ == '__main__':
    main()