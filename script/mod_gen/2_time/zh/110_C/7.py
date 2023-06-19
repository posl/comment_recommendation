def main():
    S = input()
    T = input()
    #print(S,T)
    #print(len(S),len(T))
    #print(len(S) == len(T))
    #print(S.islower(),T.islower())
    #print(S.isalpha(),T.isalpha())
    if len(S) == len(T) and S.islower() and T.islower() and S.isalpha() and T.isalpha():
        S_list = list(S)
        T_list = list(T)
        S_list.sort()
        T_list.sort()
        #print(S_list)
        #print(T_list)
        if S_list == T_list:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

if __name__ == '__main__':
    main()