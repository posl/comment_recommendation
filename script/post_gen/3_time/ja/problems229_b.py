Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    if a+b > 10**18:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A+B<10:
        print("Easy")
    else:
        print("Hard")

main()

=======
Suggestion 3

def main():
    A,B = map(int,input().split())
    if A+B >= 10:
        print('Hard')
    else:
        print('Easy')

=======
Suggestion 4

def main():
    a,b=map(int,input().split())
    if a+b>=10**18:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 5

def main():
    A,B = map(int, input().split())
    if A+B < 10**18:
        print("Easy")
    else:
        print("Hard")

=======
Suggestion 6

def main():
    A,B = map(int,input().split())
    if (A+B) >= 10:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 7

def main():
    a,b=map(int,input().split())
    if a+b>999999999:
        print("Hard")
    else:
        print("Easy")

=======
Suggestion 8

def main():
    A, B = map(int, input().split())
    ans = "Hard"
    if A + B < 10:
        ans = "Easy"
    print(ans)

=======
Suggestion 9

def main():
    A, B = map(int, input().split())
    print("Easy" if A+B < 10 else "Hard")

=======
Suggestion 10

def main():
    #入力
    A,B = map(int,input().split())
    #A+Bを計算
    C = A+B
    #A+Bを文字列に変換
    C = str(C)
    #Cの桁数を取得
    C_len = len(C)
    #Cの各桁の値を取得
    C_list = list(map(int,C))
    #繰り上がりフラグ
    flag = 0
    #Cの各桁の値が10以上の場合
    for i in range(C_len):
        if C_list[i] >= 10:
            flag = 1
            break
    #繰り上がりフラグにより出力
    if flag == 0:
        print("Easy")
    else:
        print("Hard")
