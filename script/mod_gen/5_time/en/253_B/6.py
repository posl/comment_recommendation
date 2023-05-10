def main():
    H, W = map(int, input().split())
    S = [input() for _ in range(H)]
    print(S)
    print(H, W)
    print(S[0][2])
    print(S[1][0])
    print(S[1][1])

if __name__ == '__main__':
    main()