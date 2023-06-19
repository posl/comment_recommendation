def main():
    S = input()
    T = input()
    S_list = list(S)
    T_list = list(T)
    if S_list[0] == T_list[0] and S_list[1] == T_list[1]:
        print("Yes")
    elif S_list[0] == T_list[1] and S_list[1] == T_list[0]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()