Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    T = input()
    ans = len(T)
    for i in range(len(S) - len(T) + 1):
        cnt = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

main()

The code is self-explanatory. I just iterate through all possible positions of T in S and count the number of characters that need to be changed. The minimum of these is the answer.

=======
Suggestion 2

def main():
    S = input()
    T = input()
    ans = 1000
    for i in range(len(S)-len(T)+1):
        cnt = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 3

def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    ans = 1000
    for i in range(N-M+1):
        cnt = 0
        for j in range(M):
            if S[i+j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    T = input()
    N = len(S)
    M = len(T)
    ans = M
    for i in range(N-M+1):
        tmp = 0
        for j in range(M):
            if S[i+j] != T[j]:
                tmp += 1
        ans = min(ans, tmp)
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    T = input()
    min = 1000
    for i in range(len(S)-len(T)+1):
        count = 0
        for j in range(len(T)):
            if S[i+j] != T[j]:
                count += 1
        if count < min:
            min = count
    print(min)

main()

=======
Suggestion 6

def main():
    S = input()
    T = input()
    lenS = len(S)
    lenT = len(T)
    minChanges = lenT
    for i in range(lenS - lenT + 1):
        changes = 0
        for j in range(lenT):
            if S[i + j] != T[j]:
                changes += 1
        if changes < minChanges:
            minChanges = changes
    print(minChanges)

=======
Suggestion 7

def main():
    S = input()
    T = input()
    N = len(T)
    M = len(S)
    ans = N
    for i in range(M - N + 1):
        cnt = 0
        for j in range(N):
            if S[i + j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 8

def main():
    S = input()
    T = input()
    S_len = len(S)
    T_len = len(T)
    ans = 10**6
    for i in range(S_len-T_len+1):
        cnt = 0
        for j in range(T_len):
            if S[i+j] != T[j]:
                cnt += 1
        ans = min(ans, cnt)
    print(ans)

=======
Suggestion 9

def check(s, t):
    for i in range(len(s)):
        if t == s[i:i+len(t)]:
            return True
    return False

=======
Suggestion 10

def read():
    return raw_input()
