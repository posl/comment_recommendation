Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    k = int(input())
    count = 0
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
    print(min(count+2*k,len(s)-1))

=======
Suggestion 2

def main():
    s = input()
    k = int(input())
    count = 0
    for i in range(len(s)):
        if i == 0:
            if s[i] == "X":
                count += 1
        elif s[i] == "X":
            if s[i-1] == "X":
                count += 1
            else:
                count = 1
        else:
            count = 0
        if count >= k:
            count = k
            break
    print(count)

=======
Suggestion 3

def main():
    S = input()
    K = int(input())
    S = S.replace('X', '0').replace('.', '1')
    S = S.split('0')
    S = [len(s) for s in S]
    S = [s - 1 for s in S if s > 0]
    S = [0] + S + [0]
    for i in range(len(S) - 1):
        S[i + 1] += S[i]
    ans = 0
    for i in range(0, len(S), 2):
        if i + 2 * K + 1 < len(S):
            ans = max(ans, S[i + 2 * K + 1] - S[i])
        else:
            ans = max(ans, S[-1] - S[i])
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    K = int(input())
    S = S.replace(".","X")
    X = 0
    for i in range(len(S)-1):
        if S[i] == "X":
            if S[i+1] == "X":
                X += 1
    if K == 0:
        print(X)
    else:
        if S[0] == "X":
            if S[-1] == "X":
                print(X+K*2)
            else:
                print(X+K)
        else:
            if S[-1] == "X":
                print(X+K)
            else:
                print(X+K-1)

=======
Suggestion 5

def main():
    s = input()
    k = int(input())
    n = len(s)
    if n == 1:
        print(k//2)
        return
    if n == 2:
        if s[0] == s[1]:
            print(k)
            return
        else:
            print(0)
            return

    if s[0] == s[n-1]:
        if s[0] == s[n-2]:
            if s[0] == s[n-3]:
                print((k//2)*3+1)
                return
            else:
                print((k//2)*3)
                return
        else:
            print((k//2)*2)
            return
    else:
        print((k//2)*2)
        return

=======
Suggestion 6

def main():
    s = input()
    k = int(input())
    s = s.replace("X", "X.")
    s = s.split(".")
    max_len = 0
    for i in range(len(s)):
        max_len = max(max_len, len(s[i]))
    if len(s) - 1 <= k:
        print(len(s) - 1)
    else:
        print(max_len)

=======
Suggestion 7

def main():
    S = input()
    K = int(input())
    s = S.replace(".","X")
    s = s.replace("X"*K,"."*K)
    print(len(s))

=======
Suggestion 8

def main():
    S = input()
    K = int(input())
    N = len(S)
    tmp = 0
    cnt = 0
    for i in range(N):
        if S[i] == "X":
            tmp += 1
        else:
            cnt += tmp*(tmp+1)//2
            tmp = 0
    cnt += tmp*(tmp+1)//2
    if K == 0:
        print(cnt)
        exit()
    if S[0] == "X":
        tmp = 1
    else:
        tmp = 0
    for i in range(1,N):
        if S[i] == "X":
            tmp += 1
        else:
            break
    if tmp > 0:
        cnt -= tmp*(tmp+1)//2
    if S[-1] == "X":
        tmp = 1
    else:
        tmp = 0
    for i in range(1,N):
        if S[-i-1] == "X":
            tmp += 1
        else:
            break
    if tmp > 0:
        cnt -= tmp*(tmp+1)//2
    for i in range(1,N-1):
        if S[i] == "X" and S[i-1] == "." and S[i+1] == ".":
            cnt -= 1
    print(cnt+K*2)

=======
Suggestion 9

def main():
    S = input()
    K = int(input())
    S += 'X'
    cnt = 0
    for i in range(len(S)-1):
        if S[i] == 'X':
            cnt += 1
        else:
            if S[i+1] == 'X':
                cnt += 1
            else:
                if K > 0:
                    cnt += 1
                    K -= 1
    print(cnt)

=======
Suggestion 10

def main():
    S = input()
    K = int(input())
    count = 0
    for i in range(len(S)-1):
        if S[i] == S[i+1]:
            count += 1
    count = min(count+2*K,len(S)-1)
    print(count)
main()
