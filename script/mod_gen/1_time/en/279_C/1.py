def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    T = [input() for _ in range(H)]
    print('Yes' if sorted(S) == sorted(T) else 'No')

if __name__ == '__main__':
    main()