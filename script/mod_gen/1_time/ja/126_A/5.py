def main():
    N, K = map(int, input().split())
    S = input()
    print(S[:K - 1] + S[K - 1].lower() + S[K:])
    return

if __name__ == '__main__':
    main()