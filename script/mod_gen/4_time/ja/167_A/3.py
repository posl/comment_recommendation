def main():
    S = input()
    T = input()
    if S + 'a' == T:
        print('Yes')
    elif S + 'z' == T:
        print('Yes')
    elif S + 'zz' == T:
        print('Yes')
    elif S + 'zzz' == T:
        print('Yes')
    elif S + 'zzzz' == T:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()