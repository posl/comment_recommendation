Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    abc = input()
    bca = abc[1] + abc[2] + abc[0]
    cab = abc[2] + abc[0] + abc[1]
    print(int(abc) + int(bca) + int(cab))

=======
Suggestion 2

def main():
    abc = input()
    print(int(abc) + int(abc[1] + abc[2] + abc[0]) + int(abc[2] + abc[0] + abc[1]))

=======
Suggestion 3

def main():
    abc = input()
    x = abc[0]
    y = abc[1]
    z = abc[2]
    xyz = int(x+y+z)
    bca = int(y+z+x)
    cab = int(z+x+y)
    print(xyz+bca+cab)

=======
Suggestion 4

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a+b+c, b+c+a, c+a+b, sep='')

=======
Suggestion 5

def main():
    abc = input()
    a = abc[0]
    b = abc[1]
    c = abc[2]
    xyz = int(a+b+c) + int(b+c+a) + int(c+a+b)
    print(xyz)

=======
Suggestion 6

def main():
    abc = input()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(a+b+c+a*c+b*c+a*b)

=======
Suggestion 7

def main():
    abc = int(input())
    #print(abc)
    a = abc // 100
    b = (abc - a * 100) // 10
    c = abc % 10
    #print(a,b,c)
    print(a+b+c + b+c+a + c+a+b)

=======
Suggestion 8

def main():
    abc = input()
    print(int(abc) + int(abc[1:]+abc[0]) + int(abc[2]+abc[:2]))

=======
Suggestion 9

def main():
    a,b,c = map(int, input().split())
    print(a+b+c+a*100+b*10+c)

=======
Suggestion 10

def main():
    #入力
    abc = input()
    #abcをリストにする
    abc_list = list(abc)
    #print(abc_list)
    #abcをリストにする
    bca_list = [abc_list[1],abc_list[2],abc_list[0]]
    #print(bca_list)
    #abcをリストにする
    cab_list = [abc_list[2],abc_list[0],abc_list[1]]
    #print(cab_list)
    #リストを文字列に変換
    bca = "".join(bca_list)
    #print(bca)
    #リストを文字列に変換
    cab = "".join(cab_list)
    #print(cab)
    #出力
    print(int(abc)+int(bca)+int(cab))
