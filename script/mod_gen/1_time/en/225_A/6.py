def main():
    S = input()
    if S[0] == S[1] and S[1] == S[2]:
        print(1)
    elif S[0] != S[1] and S[1] != S[2] and S[0] != S[2]:
        print(6)
    else:
        print(3)

if __name__ == '__main__':
    main()