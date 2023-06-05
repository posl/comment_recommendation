def main():
    n = int(input())
    s = [input() for _ in range(n)]
    # 2^n - 1
    print(2 ** n - 1)

if __name__ == '__main__':
    main()