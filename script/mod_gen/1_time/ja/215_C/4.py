def main():
    S, K = input().split()
    K = int(K)
    S = list(S)
    S.sort()
    S = "".join(S)
    print(S)
    print(S[K-1])

if __name__ == '__main__':
    main()