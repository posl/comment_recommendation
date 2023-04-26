Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    abc = input()
    bca = abc[1] + abc[2] + abc[0]
    cab = bca[1] + bca[2] + bca[0]
    print(int(abc) + int(bca) + int(cab))

=======
Suggestion 2

def main():
    abc = int(input())
    a = abc // 100
    b = (abc - a * 100) // 10
    c = abc - a * 100 - b * 10
    print(abc + b * 100 + c * 10 + a + b * 10 + c)

=======
Suggestion 3

def main():
    abc = list(input())
    bca = [abc[1], abc[2], abc[0]]
    cab = [abc[2], abc[0], abc[1]]
    print(int("".join(abc)) + int("".join(bca)) + int("".join(cab)))

=======
Suggestion 4

def main():
    a,b,c = map(int,input().split())
    print(a*100+b*10+c+b*100+c*10+a+c*100+a*10+b)

=======
Suggestion 5

def main():
    abc = input()
    a,b,c = abc[0],abc[1],abc[2]
    print(int(a+b+c)+int(b+c+a)+int(c+a+b))

=======
Suggestion 6

def main():
    abc = int(input())
    a = abc//100
    b = (abc%100)//10
    c = (abc%100)%10
    print(a+b+c + b+c+a + c+a+b)

=======
Suggestion 7

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a+b+c+a*100+b*10+c, a+c+c*100+a*10+b, b+c+c*100+a*10+b, sep=' + ')

=======
Suggestion 8

def main():
    #入力
    abc = input()
    #abcをリストに変換
    abc_list = list(abc)
    #abcをリストに変換
    bca_list = abc_list[1:] + abc_list[:1]
    #abcをリストに変換
    cab_list = abc_list[2:] + abc_list[:2]
    #リストを文字列に変換
    bca = ''.join(bca_list)
    #リストを文字列に変換
    cab = ''.join(cab_list)
    #出力
    print(int(abc) + int(bca) + int(cab))

=======
Suggestion 9

def main():
    # 3つの数字を入力
    abc = input()
    # 3つの数字をリストに格納
    abc_list = list(abc)
    # 3つの数字をリストに格納
    bca_list = abc_list[1:] + abc_list[:1]
    # 3つの数字をリストに格納
    cab_list = abc_list[2:] + abc_list[:2]
    # 3つの数字をリストに格納
    xyz_list = [abc, ''.join(bca_list), ''.join(cab_list)]
    # 3つの数字をリストに格納
    xyz = int(''.join(xyz_list))
    # 3つの数字をリストに格納
    print(xyz)

=======
Suggestion 10

def main():
    #入力
    abc = input()
    #文字列を整数に変換
    abc = int(abc)
    #文字列の長さを取得
    length = len(str(abc))
    #文字列をリストに変換
    abc_list = list(str(abc))
    #リストの中身を整数に変換
    abc_list = list(map(int,abc_list))
    #変数の初期化
    bca_list = []
    cab_list = []
    #リストの中身を入れ替える
    for i in range(length):
        bca_list.append(abc_list[(i+1)%length])
        cab_list.append(abc_list[(i+2)%length])
    #リストを文字列に変換
    bca = ''.join(map(str,bca_list))
    cab = ''.join(map(str,cab_list))
    #文字列を整数に変換
    bca = int(bca)
    cab = int(cab)
    #出力
    print(abc+bca+cab)
