def main():
    S = input()
    S = S.lower()
    S = sorted(S)
    if S[0] == S[1]:
        if S[1] == S[2]:
            print(-1)
        else:
            print(S[2])
    else:
        print(S[0])

if __name__ == '__main__':
    main()