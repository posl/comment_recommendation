def main():
    S = input()
    if S[0] != S[1] and S[0] != S[2]:
        print(S[0])
    elif S[1] != S[0] and S[1] != S[2]:
        print(S[1])
    elif S[2] != S[0] and S[2] != S[1]:
        print(S[2])
    else:
        print(-1)

if __name__ == '__main__':
    main()