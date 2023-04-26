Synthesizing 10/10 solutions (Duplicates hidden)

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

main()

=======
Suggestion 2

def main():
    S = input()
    ans = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    R = S.count('0')
    B = S.count('1')
    print(min(R, B) * 2)

=======
Suggestion 4

def main():
    S = input()
    print(max(S.count('0'), S.count('1')) * 2)

=======
Suggestion 5

def main():
    s = input()
    print(max(s.count('0'), s.count('1')) * 2)

=======
Suggestion 6

def main():
    # 入力
    S = input()
    N = len(S)
    # 計算
    count = 0
    for i in range(N-1):
        if S[i] != S[i+1]:
            count += 1
    # 出力
    print(count)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    print(max(S.count('0'), S.count('1'))*2)

=======
Suggestion 8

def main():
    S = input()
    print(len(S) - 1)
