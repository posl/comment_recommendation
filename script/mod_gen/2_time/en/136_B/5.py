def main():
    N = int(input())
    print(N - 9 * len(str(N)) + 1)

if __name__ == '__main__':
    main()