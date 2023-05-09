def main():
    S = input()
    T = input()
    if S == T:
        print('Yes')
        exit()
    for i in range(1, len(S)):
        S = S[-1] + S[0:-1]
        if S == T:
            print('Yes')
            exit()
    print('No')
main()

if __name__ == '__main__':
    main()