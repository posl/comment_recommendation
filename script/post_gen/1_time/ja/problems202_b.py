Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    S = S[::-1]
    S = S.replace('0', 'a')
    S = S.replace('1', 'b')
    S = S.replace('6', 'c')
    S = S.replace('8', 'd')
    S = S.replace('9', 'e')
    S = S.replace('a', '9')
    S = S.replace('b', '1')
    S = S.replace('c', '6')
    S = S.replace('d', '8')
    S = S.replace('e', '0')
    print(S)

=======
Suggestion 2

def main():
    s = input()
    ans = ""
    for i in s:
        if i == "6":
            ans = "9" + ans
        elif i == "9":
            ans = "6" + ans
        else:
            ans = i + ans
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    S = S[::-1]
    S = S.replace("6","a")
    S = S.replace("9","6")
    S = S.replace("a","9")
    print(S)

=======
Suggestion 4

def main():
    S = input()
    S = S[::-1]
    S = S.replace("0", "o")
    S = S.replace("1", "i")
    S = S.replace("6", "9")
    S = S.replace("8", "8")
    S = S.replace("9", "6")
    S = S.replace("o", "0")
    S = S.replace("i", "1")
    print(S)

=======
Suggestion 5

def main():
    S = input()
    S = S[::-1]
    S = S.replace('0','o')
    S = S.replace('1','i')
    S = S.replace('6','9')
    S = S.replace('8','8')
    S = S.replace('9','6')
    S = S.replace('o','0')
    S = S.replace('i','1')
    print(S)

=======
Suggestion 6

def main():
    S = input()
    S = S[::-1]
    S = S.replace('0', 't')
    S = S.replace('1', 'o')
    S = S.replace('6', 'n')
    S = S.replace('8', 'e')
    S = S.replace('9', 's')
    S = S.replace('t', '9')
    S = S.replace('o', '1')
    S = S.replace('n', '6')
    S = S.replace('e', '8')
    S = S.replace('s', '0')
    print(S)

=======
Suggestion 7

def main():
    S = input()
    S = S[::-1]
    S = S.replace('6','9')
    S = S.replace('9','6')
    print(S)

=======
Suggestion 8

def main():
    S=input()
    S=S[::-1]
    S=S.replace('6','x')
    S=S.replace('9','6')
    S=S.replace('x','9')
    print(S)

=======
Suggestion 9

def main():
    S = input()
    print(S[::-1].replace('6','a').replace('9','6').replace('a','9'))

=======
Suggestion 10

def main():
    # 入力
    S = input()
    # 処理
    S = S[::-1] # 反転
    S = S.replace('6', 'x') # 6をxに置換
    S = S.replace('9', '6') # 9を6に置換
    S = S.replace('x', '9') # xを9に置換
    # 出力
    print(S)
