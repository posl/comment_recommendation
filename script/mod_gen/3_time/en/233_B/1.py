def main():
    L, R = map(int, input().split())
    S = input()
    S = S[:L-1] + S[L-1:R][::-1] + S[R:]
    print(S)

if __name__ == '__main__':
    main()