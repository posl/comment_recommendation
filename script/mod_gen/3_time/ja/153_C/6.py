def main():
    N, K = map(int, input().split())
    H = list(map(int, input().split()))
    H = sorted(H,reverse=True)
    ans = 0
    for i in range(N):
        if i < K:
            continue
        else:
            ans += H[i]
    print(ans)

if __name__ == '__main__':
    main()