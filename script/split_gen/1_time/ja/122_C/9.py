def main():
    N,Q = map(int,input().split())
    S = input()
    #print(N,Q,S)
    l = []
    r = []
    for i in range(Q):
        l_i,r_i = map(int,input().split())
        l.append(l_i)
        r.append(r_i)
    #print(l)
    #print(r)
    #文字列のACの数をカウント
    #ACの数をカウントするためには、ACで始まる文字列の数とACで終わる文字列の数をそれぞれカウントすれば良い
    #ACで始まる文字列の数をカウントするためには、Sの先頭から2文字目以降でACが出現する回数をカウント
    #ACで終わる文字列の数をカウントするためには、Sの末尾から2文字目以前でACが出現する回数をカウント
    #ACで始まる文字列の数とACで終わる文字列の数をそれぞれカウントし、その積がACの数になる
    #ACで始まる文字列の数をカウントするためには、Sの先頭から2文字目以降でACが出現する回数をカウント
    #ACで終わる文字列の数をカウントするためには、Sの末尾から2文字目以前でACが出現する回数をカウント
    #ACで始まる文字列の数とACで終わる文字列の数をそれぞれカウントし、その積がACの数になる
    #ACで始まる文字列の数をカウントするためには、Sの先頭から2文字目以降でACが出現する回数をカウント
    #ACで終わる文字列の数をカウントするためには、Sの末尾から2文字目以前でACが出現する
