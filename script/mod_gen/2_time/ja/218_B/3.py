def main():
    P = list(map(int, input().split()))
    S = []
    for i in range(26):
        S.append(chr(P[i]+96))
    print(''.join(S))

if __name__ == '__main__':
    main()