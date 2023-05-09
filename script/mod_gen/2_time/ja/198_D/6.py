def main():
    s1 = input()
    s2 = input()
    s3 = input()
    #文字列の長さが違う場合は解けない
    if len(s1) != len(s2) or len(s2) != len(s3):
        print('UNSOLVABLE')
        return
    #文字列の文字数をカウント
    c1 = [0]*26
    c2 = [0]*26
    c3 = [0]*26
    for i in range(len(s1)):
        c1[ord(s1[i])-97] += 1
        c2[ord(s2[i])-97] += 1
        c3[ord(s3[i])-97] += 1
    #文字列の文字数が同じであるかチェック
    for i in range(26):
        if c1[i] != c2[i] or c1[i] != c3[i]:
            print('UNSOLVABLE')
            return
    #各文字列の先頭文字が0の場合は解けない
    if s1[0] == '0' or s2[0] == '0' or s3[0] == '0':
        print('UNSOLVABLE')
        return
    #文字列を数字に変換
    n1 = int(s1)
    n2 = int(s2)
    n3 = int(s3)
    #各文字列の先頭文字を1~9に置換して試す
    for i in range(1,10):
        for j in range(1,10):
            for k in range(1,10):
                if s1.count(str(i)) == 1 and s2.count(str(j)) == 1 and s3.count(str(k)) == 1:
                    if n1 - n1//10*10 == i and n2 - n2//10*10 == j and n3 - n3//10*10 == k:
                        if n1 + n2 == n3:
                            print(n1)
                            print(n2)
                            print(n3)
                            return
    print('UNSOLVABLE')

if __name__ == '__main__':
    main()