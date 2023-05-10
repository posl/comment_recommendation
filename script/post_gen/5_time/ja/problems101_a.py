Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    result = 0
    for i in range(len(s)):
        if s[i] == '+':
            result += 1
        else:
            result -= 1
    print(result)

=======
Suggestion 2

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == "+":
            ans += 1
        else:
            ans -= 1
    print(ans)

main()

=======
Suggestion 3

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == "+":
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 4

def main():
    s = input()
    ans = 0
    for i in range(4):
        if s[i] == '+':
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 5

def main():
    s = input()
    print(s.count('+') - s.count('-'))

=======
Suggestion 6

def main():
    # 標準入力受け取り
    S = input()
    # 処理
    ans = 0
    for i in range(4):
        if S[i] == '+':
            ans += 1
        elif S[i] == '-':
            ans -= 1
    # 出力
    print(ans)

=======
Suggestion 7

def main():
    S = input()
    count = 0
    for i in range(4):
        if S[i] == '+':
            count += 1
        else:
            count -= 1
    print(count)

=======
Suggestion 8

def main():
    # your code here
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == "+":
            ans += 1
        else:
            ans -= 1
    print(ans)

=======
Suggestion 9

def main():
    # 文字列の入力
    S = input()
    # 出力
    print(S.count("+") - S.count("-"))
