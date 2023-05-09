def main():
    P = list(map(int, input().split()))
    S = [chr(ord('a') + i) for i in range(26)]
    for i in range(26):
        S[i], S[P[i] - 1] = S[P[i] - 1], S[i]
    print(''.join(S))

if __name__ == '__main__':
    main()