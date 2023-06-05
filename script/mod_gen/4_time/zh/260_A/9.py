def main():
    S = input()
    if S[0] == S[1] and S[0] != S[2]:
        print(S[2])
    elif S[0] == S[2] and S[0] != S[1]:
        print(S[1])
    elif S[1] == S[2] and S[0] != S[1]:
        print(S[0])
    else:
        print(-1)

if __name__ == '__main__':
    main()