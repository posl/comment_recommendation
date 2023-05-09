def main():
    N = int(input())
    S = input()
    c = 0
    for i in range(N):
        if S[i] == '"':
            c += 1
        if S[i] == ',' and c % 2 == 0:
            S = S[:i] + '.' + S[i+1:]
    print(S)

if __name__ == '__main__':
    main()