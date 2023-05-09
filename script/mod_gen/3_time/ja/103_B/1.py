def main():
    S = input()
    T = input()
    for i in range(len(S)):
        S = S[-1] + S[:-1]
        if S == T:
            print('Yes')
            break
    else:
        print('No')

if __name__ == '__main__':
    main()