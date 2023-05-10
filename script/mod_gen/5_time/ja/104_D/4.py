def calcABCNum(s):
    #sの中にあるABC数を計算する
    #sの長さが3未満の場合は0を返す
    if len(s) < 3:
        return 0
    #sの先頭の文字がAでない場合は、先頭の文字を削除して再帰呼び出し
    if s[0] != 'A':
        return calcABCNum(s[1:])
    #sの先頭から2文字目の文字がBでない場合は、先頭の文字を削除して再帰呼び出し
    if s[1] != 'B':
        return calcABCNum(s[1:])
    #sの先頭から3文字目の文字がCでない場合は、先頭の文字を削除して再帰呼び出し
    if s[2] != 'C':
        return calcABCNum(s[1:])
    #sの先頭から3文字目までがABCの場合は、先頭の文字を削除して再帰呼び出し
    return 1 + calcABCNum(s[1:])
s = input()
s = s.replace('?', 'A')
print(calcABCNum(s))

if __name__ == '__main__':
    calcABCNum()