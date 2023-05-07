def main():
    N = int(input())
    S = input()
    i = 0
    while i < N:
        if S[i] == '"':
            i += 1
            while S[i] != '"':
                if S[i] == ',':
                    S = S[:i] + '.' + S[i+1:]
                i += 1
        i += 1
    print(S)

if __name__ == '__main__':
    main()