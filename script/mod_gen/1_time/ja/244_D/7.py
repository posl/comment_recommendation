def main():
    S = input().split()
    T = input().split()
    if S == T:
        print('Yes')
    elif S[0] == S[1] and S[0] == S[2]:
        print('No')
    elif S[0] == S[1] and T[0] == T[1]:
        print('Yes')
    elif S[1] == S[2] and T[1] == T[2]:
        print('Yes')
    elif S[0] == S[2] and T[0] == T[2]:
        print('Yes')
    else:
        print('No')
main()

if __name__ == '__main__':
    main()