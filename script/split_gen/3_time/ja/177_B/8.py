def main():
    S = input()
    T = input()
    #Sの文字数
    s_len = len(S)
    #Tの文字数
    t_len = len(T)
    #Tの文字数がSの文字数より多い場合は-1を出力
    if s_len < t_len:
        print(-1)
        return
    #Sの文字数がTの文字数より多い場合はSの文字数を出力
    if s_len >= t_len:
        print(s_len)
        return
