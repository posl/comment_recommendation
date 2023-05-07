def main():
    L, R = map(int, input().split())
    S = list(input())
    S[L-1:R] = S[L-1:R][::-1]
    print(''.join(S))

if __name__ == '__main__':
    main()