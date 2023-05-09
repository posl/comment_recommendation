def main():
    S = input()
    N = len(S)
    if N == 1:
        print(0)
        return
    if N == 2:
        if S == '00' or S == '11':
            print(0)
        else:
            print(1)
        return
    if S[0] == S[1]:
        print(1 + main(S[1:]))
    else:
        print(2 + main(S[2:]))

if __name__ == '__main__':
    main()