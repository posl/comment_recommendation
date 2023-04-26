Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S, T = map(int, input().split())
    ans = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a+b+c <= S and a*b*c <= T:
                    ans += 1
    print(ans)

=======
Suggestion 2

def main():
    S, T = map(int, input().split())
    count = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a + b + c <= S and a * b * c <= T:
                    count += 1
    print(count)

=======
Suggestion 3

def main():
    s, t = map(int, input().split())
    cnt = 0
    for a in range(s+1):
        for b in range(s+1):
            for c in range(s+1):
                if a + b + c <= s and a * b * c <= t:
                    cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    S, T = map(int, input().split())
    cnt = 0
    for i in range(S+1):
        for j in range(S+1):
            for k in range(S+1):
                if i+j+k <= S and i*j*k <= T:
                    cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    S, T = map(int,input().split())
    count = 0
    for a in range(0,S+1):
        for b in range(0,S+1):
            for c in range(0,S+1):
                if (a+b+c <= S) and (a*b*c <= T):
                    count += 1
    print(count)

=======
Suggestion 6

def main():
    # 入力
    S, T = map(int, input().split())

    # 処理
    ans = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a+b+c <= S and a*b*c <= T:
                    ans += 1

    # 出力
    print(ans)

=======
Suggestion 7

def main():
    #入力
    S, T = map(int, input().split())

    #計算
    count = 0
    for a in range(S+1):
        for b in range(S+1):
            for c in range(S+1):
                if a+b+c <= S and a*b*c <= T:
                    count += 1

    #出力
    print(count)
