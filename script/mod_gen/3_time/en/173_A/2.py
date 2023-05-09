def main():
    N = int(input())
    print(N % 1000 if N % 1000 != 0 else 1000)

if __name__ == '__main__':
    main()