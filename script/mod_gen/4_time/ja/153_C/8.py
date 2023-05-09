def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    H = H[K:]
    print(sum(H))
main()

if __name__ == '__main__':
    main()