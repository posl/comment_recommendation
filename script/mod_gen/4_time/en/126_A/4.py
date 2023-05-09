def main():
    # input
    N, K = map(int, input().split())
    S = input()
    # output
    print(S[:K-1]+S[K-1].lower()+S[K:])

if __name__ == '__main__':
    main()