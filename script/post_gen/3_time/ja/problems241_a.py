Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    k = 0
    for i in range(3):
        k = a[k]
    print(k)

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    num = 0
    for i in range(3):
        num = a[num]
    print(num)

=======
Suggestion 3

def main():
    #入力
    a = list(map(int, input().split()))
    #処理
    k = 0
    for i in range(3):
        k = a[k]
    #出力
    print(k)

=======
Suggestion 4

def main():
    a = list(map(int, input().split()))
    for i in range(3):
        a[0] = a[a[0]]
    print(a[0])

=======
Suggestion 5

def main():
    #入力
    a = list(map(int, input().split()))
    #処理
    ans = 0
    for i in range(3):
        ans = a[ans]
    #出力
    print(ans)

=======
Suggestion 6

def main():
    a = list(map(int, input().split()))
    print(a[0])

=======
Suggestion 7

def main():
    # 1行目の入力
    a = list(map(int,input().split()))
    # 0が表示されている状態からボタンを3回押すと、画面には何が表示されるか
    print(a[a[a[0]]])

=======
Suggestion 8

def main():
    a = list(map(int, input().split()))
    print(a[a[0]])

=======
Suggestion 9

def main():
    a = input().split()
    v = 0
    for i in range(3):
        v = a[v]
    print(v)
