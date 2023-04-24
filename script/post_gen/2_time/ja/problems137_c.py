Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    S.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if S[i] == S[j]:
                continue
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

=======
Suggestion 3

def main():
    n = int(input())
    s = [input() for _ in range(n)]
    ans = 0
    for i in range(n-1):
        for j in range(i+1,n):
            if sorted(s[i]) == sorted(s[j]):
                ans += 1
    print(ans)

=======
Suggestion 4

def main():
    N = int(input())
    s = [input() for i in range(N)]
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(s[i]) == sorted(s[j]):
                ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    s = [input() for _ in range(N)]
    s.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if s[i] == s[j]:
                continue
            if "".join(sorted(s[i])) == "".join(sorted(s[j])):
                ans += 1
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    s = [input() for _ in range(N)]
    s.sort()
    cnt = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if len(s[i]) != len(s[j]):
                break
            if sorted(s[i]) == sorted(s[j]):
                cnt += 1
    print(cnt)

=======
Suggestion 8

def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    S.sort()
    cnt = 0
    for i in range(N):
        for j in range(i+1, N):
            if sorted(S[i]) == sorted(S[j]):
                cnt += 1
    print(cnt)

=======
Suggestion 9

def main():
    N = int(input())
    S = [input() for i in range(N)]
    S.sort()
    #print(S)
    ans = 0
    for i in range(N-1):
        for j in range(i+1,N):
            if S[i] == S[j]:
                continue
            else:
                if sorted(S[i]) == sorted(S[j]):
                    ans += 1
    print(ans)

=======
Suggestion 10

def main():
    N = int(input())
    S = [input() for _ in range(N)]

    # ここに処理を書く
    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            #print(i,j)
            if sorted(S[i]) == sorted(S[j]):
                ans += 1
    print(ans)
