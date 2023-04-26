Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    ans = -1
    for i in range(len(s)):
        if s[i] == 'a':
            ans = i + 1
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    if 'a' in s:
        print(len(s) - s[::-1].index('a'))
    else:
        print(-1)

main()

=======
Suggestion 3

def main():
    s = input()
    if 'a' in s:
        print(len(s) - s[::-1].index('a'))
    else:
        print(-1)

=======
Suggestion 4

def main():
    s = input()
    if 'a' in s:
        print(s.rfind('a') + 1)
    else:
        print(-1)

=======
Suggestion 5

def main():
    #入力
    s = input()
    #S に a が現れるならば最後に現れるのが何文字目かを出力し、現れないならば -1 を出力してください。
    #S は英小文字からなる長さ 1 以上 100 以下の文字列
    if "a" in s:
        print(s.rfind("a") + 1)
    else:
        print(-1)

=======
Suggestion 6

def main():
    S = input()
    if S.count('a') == 0:
        print(-1)
    else:
        print(len(S) - S[::-1].index('a'))

=======
Suggestion 7

def main():
    S = input()
    print(S.rfind('a')+1 if 'a' in S else -1)

=======
Suggestion 8

def main():
    s = input()
    print(len(s) - s[::-1].index('a') - 1 if 'a' in s else -1)

=======
Suggestion 9

def main():
    s = input()
    print(s.rfind("a") + 1 if "a" in s else -1)

=======
Suggestion 10

def main():
    s = input()
    print(s.rfind("a")+1 if s.rfind("a")!=-1 else -1)
