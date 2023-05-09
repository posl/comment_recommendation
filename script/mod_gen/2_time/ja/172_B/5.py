def main():
    #入力
    S = input()
    T = input()
    #Sの文字列をリストに分割
    S_list = list(S)
    #Tの文字列をリストに分割
    T_list = list(T)
    #Tの文字列とSの文字列を比較
    count = 0
    for i in range(len(S)):
        if S_list[i] != T_list[i]:
            count += 1
    print(count)

if __name__ == '__main__':
    main()