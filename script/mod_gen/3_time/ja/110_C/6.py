def main():
    S = input()
    T = input()
    S = S.lower()
    T = T.lower()
    S_list = list(S)
    T_list = list(T)
    S_list.sort()
    T_list.sort()
    if S_list == T_list:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()