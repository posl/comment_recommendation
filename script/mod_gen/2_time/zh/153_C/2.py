def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort()
    H.reverse()
    print(sum(H[K:]))

if __name__ == '__main__':
    main()