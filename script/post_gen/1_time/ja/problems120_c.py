Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    N = len(S)
    ans = 0
    for i in range(N-1):
        if S[i] != S[i+1]:
            ans += 2
    print(ans)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    count = 0
    for i in range(N-1):
        if S[i] != S[i+1]:
            count += 2
    print(count)

=======
Suggestion 3

def main():
    S = input()
    print(max(S.count("0"), S.count("1")) * 2)

=======
Suggestion 4

def main():
    s = input()
    print(max(s.count('0'), s.count('1')) * 2)

=======
Suggestion 5

def main():
    S = input()
    N = len(S)
    #print(S)
    #print(N)
    red = 0
    blue = 0
    for i in range(N):
        if S[i] == "0":
            red += 1
        else:
            blue += 1
    print(min(red, blue)*2)

=======
Suggestion 6

def main():
    #入力
    s = input()
    #初期化
    ans = 0
    #処理
    for i in range(len(s)-1):
        if s[i] != s[i+1]:
            ans += 2
    #出力
    print(ans)

=======
Suggestion 7

def main():
    #input
    S = input()
    N = len(S)
    #compute
    reds = S.count('0')
    blues = S.count('1')
    #output
    print(min(reds,blues)*2)

=======
Suggestion 8

def main():
    s = input()
    print(min(s.count("0"),s.count("1"))*2)

=======
Suggestion 9

def main():
    S = input()
    #print(S)
    #print(len(S))
    #print(S[0])
    #print(S[1])
    #print(S[2])
    #print(S[3])

    count = 0
    for i in range(0,len(S)-1):
        if S[i] == S[i+1]:
            count += 1
    print(count)

=======
Suggestion 10

def main():
    s = input()
    print(s.count("0") + s.count("1"))
