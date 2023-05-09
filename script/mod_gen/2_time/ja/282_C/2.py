def main():
    N = int(input())
    S = input()
    count = 0
    for i in range(N):
        if S[i] == '"':
            count += 1
        elif S[i] == ',' and count % 2 == 1:
            S = S[:i] + '.' + S[i+1:]
    print(S)

if __name__ == '__main__':
    main()