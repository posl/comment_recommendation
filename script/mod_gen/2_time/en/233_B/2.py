def main():
    L, R = map(int, input().split())
    S = list(input())
    S[L-1:R] = reversed(S[L-1:R])
    print(''.join(S))

if __name__ == '__main__':
    main()