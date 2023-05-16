def main():
    N = int(input())
    S = []
    T = []
    for _ in range(N):
        s,t = input().split()
        S.append(s)
        T.append(t)
    
    # 2人以上のユーザが同じユーザ名を希望する場合
    # そのユーザ名を変更することはできない
    # そのため、同じユーザ名を希望するユーザがいないかを確認する
    if len(S) != len(set(S)) or len(T) != len(set(T)):
        print("No")
        exit()
    
    # 2人以上のユーザが同じユーザ名を現在のユーザ名としている場合
    # そのユーザ名を変更することはできない
    # そのため、同じユーザ名を現在のユーザ名としているユーザがいないかを確認する
    if len(set(S)) != len(set(T)):
        print("No")
        exit()
    
    # 2人以上のユーザが同じユーザ名を現在のユーザ名としている場合
    # そのユーザ名を変更することはできない
    # そのため、同じユーザ名を現在のユーザ名としているユーザがいないかを確認する
    if len(set(S)) != len(set(T)):
        print("No")
        exit()
    
    # 2人以上のユーザが同じユーザ名を現在のユーザ名としている場合
    # そのユーザ名を変更することはできない
    # そのため、同じユーザ名を現在のユーザ名としているユーザがいないかを確認

if __name__ == '__main__':
    main()