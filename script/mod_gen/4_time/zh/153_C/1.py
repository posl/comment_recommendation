def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H.sort(reverse=True)
    ans = sum(H)
    for i in range(K):
        ans -= H[i]
    print(ans)

if __name__ == '__main__':
    main()