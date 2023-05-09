def main():
    S = input()
    T = input()
    #Tの数をカウントする
    t_count = {}
    for t in T:
        t_count[t] = t_count.get(t, 0) + 1
    #Tの数をカウントする
    s_count = {}
    for s in S:
        s_count[s] = s_count.get(s, 0) + 1
    #Tの数をカウントする
    for t in t_count:
        #SにTの文字がない場合
        if not t in s_count:
            print("No")
            return
        #SにTの文字がある場合
        else:
            #Sの文字の数がTの文字の数以上でない場合
            if s_count[t] < t_count[t]:
                print("No")
                return
    #Sの文字の数がTの文字の数以上の場合
    print("Yes")
