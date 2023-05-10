def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    ans = sum(H[K:])
    print(ans)

if __name__ == '__main__':
    main()