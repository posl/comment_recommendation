def main():
    N, K = map(int, input().split())
    S = input()
    R = S.count('R')
    L = N - R
    ans = min(R, L) * 2 + min(K, abs(R-L))
    print(ans)

if __name__ == '__main__':
    main()