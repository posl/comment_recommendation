def main():
    n = int(input())
    s = [input() for _ in range(n)]
    t = [input() for _ in range(n)]
    print('Yes' if solve(n, s, t) else 'No')

if __name__ == '__main__':
    main()