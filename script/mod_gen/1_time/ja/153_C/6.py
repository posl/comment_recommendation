def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    print(sum(H[:-K]) if N > K else 0)

if __name__ == '__main__':
    main()