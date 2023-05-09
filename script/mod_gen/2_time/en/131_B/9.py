def main():
    N, L = map(int, input().split())
    flv = [L + i - 1 for i in range(1, N + 1)]
    minflv = min(flv)
    print(sum(flv) - minflv)

if __name__ == '__main__':
    main()