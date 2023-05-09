def main():
    S = input()
    T = input()
    #print(S)
    #print(T)
    S_list = list(S)
    T_list = list(T)
    #print(S_list)
    #print(T_list)
    S_set = set(S_list)
    T_set = set(T_list)
    #print(S_set)
    #print(T_set)
    if len(S_set) < len(T_set):
        print('No')
    else:
        print('Yes')

if __name__ == '__main__':
    main()