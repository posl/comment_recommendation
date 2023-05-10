def main():
    N = int(input())
    S = input()
    if N == 2:
        if S[0] == '"':
            print(S[0] + '.' + S[1])
        else:
            print(S[0] + '.' + S[1])
    else:
        for i in range(0, N):
            if S[i] == '"':
                for j in range(i+1, N):
                    if S[j] == '"':
                        for k in range(i+1, j):
                            if S[k] == ',':
                                S = S[:k] + '.' + S[k+1:]
                                break
                        break
        print(S)

if __name__ == '__main__':
    main()