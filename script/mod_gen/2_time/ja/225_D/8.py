def main():
    #入力
    N, Q = map(int, input().split())
    #電車の連結情報を格納するリスト
    #連結情報を格納するリストの要素は、次の3つの要素のタプルで表現する。
    #リストの要素は、(前の電車の番号, 後の電車の番号, 連結成分の番号)となっている。
    #前の電車の番号と後の電車の番号は、連結している電車の番号を格納している。
    #連結成分の番号は、連結成分の番号を格納している。
    #電車の番号は、1からNまでの番号が振られている。
    #連結成分の番号は、1からNまでの番号が振られている。
    #電車の前後に連結している電車が存在しない場合は、-1が格納されている。
    #連結成分の番号は、連結成分の先頭の電車の番号と同じとする。
    #例えば、(1, 2, 1)は、電車1の後ろに電車2が連結していることを表す。
    #電車1の前に連結している電車は存在しないため、1の前の電車の番号は-1となっている。
    #連結成分の番号は、連結成分の先頭の電車の番号と同じとする。
    #例えば、(1, 2, 1)は、電車1の後ろに電

if __name__ == '__main__':
    main()