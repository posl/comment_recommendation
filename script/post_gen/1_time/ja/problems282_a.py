Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    K = int(input())
    ans = ''
    for i in range(K):
        ans += chr(ord('A') + i)
    print(ans)

=======
Suggestion 2

def main():
    K = int(input())
    ans = ""
    for i in range(K):
        ans += chr(65+i)
    print(ans)

=======
Suggestion 3

def main():
    K = int(input())
    print(''.join([chr(i) for i in range(65, 65+K)]))

=======
Suggestion 4

def main():
    k = int(input())
    print("".join([chr(i) for i in range(ord("A"), ord("A") + k)]))

=======
Suggestion 5

def main():
    k = int(input())
    print(''.join([chr(i) for i in range(65, 65 + k)]))

=======
Suggestion 6

def main():
    K = int(input())
    print("".join([chr(i) for i in range(65, 65 + K)]))

=======
Suggestion 7

def main():
    k = int(input())
    print("".join([chr(i) for i in range(65, 65+k)]))

=======
Suggestion 8

def main():
    K = int(input())
    for i in range(65,65+K):
        print(chr(i),end="")

=======
Suggestion 9

def main():
    # 1行目の入力
    k = int(input())
    # 文字列の初期化
    s = ''
    # Aから昇順にK個繋げる
    for i in range(k):
        s += chr(ord('A') + i)
    # 出力
    print(s)
