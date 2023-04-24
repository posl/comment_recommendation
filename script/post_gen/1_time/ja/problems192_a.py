Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    X = int(input())
    if X % 100 == 0:
        print(100)
    else:
        print(100 - X % 100)

=======
Suggestion 2

def main():
    x = int(input())
    if x % 100 == 0:
        print(100)
    else:
        print(100 - (x % 100))

=======
Suggestion 3

def main():
    #入力
    X = int(input())
    #出力
    if X % 100 == 0:
        print(0)
    else:
        print(100 - X % 100)

=======
Suggestion 4

def main():
    x = int(input())
    print(100 - (x % 100))

=======
Suggestion 5

def main():
    x = int(input())
    print(100 - x % 100)

=======
Suggestion 6

def main():
    #入力
    X = int(input())
    #処理
    #Xが100の倍数の場合は0を出力
    if X % 100 == 0:
        print(0)
    #Xが100の倍数でない場合は100で割った余りを出力
    else:
        print(100 - X % 100)
