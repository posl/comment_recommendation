def main():
    N, K = map(int, input().split())
    S = input()
    K = K - 1
    print(S[:K] + S[K].lower() + S[K+1:])

if __name__ == '__main__':
    main()