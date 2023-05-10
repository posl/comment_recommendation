Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    r = s.count('0')
    b = s.count('1')
    print(min(r,b)*2)

=======
Suggestion 2

def main():
    S = input()
    N = len(S)
    #print(N)
    #print(S)
    count = 0
    #print(S[1])
    for i in range(0,N-1):
        #print(S[i])
        #print(S[i+1])
        if S[i] != S[i+1]:
            count += 1
    print(count)
main()

=======
Suggestion 3

def main():
    s = input()
    s = s[::-1]
    r = 0
    b = 0
    for i in range(len(s)):
        if s[i] == '0':
            r += 1
        else:
            b += 1
        if r == b:
            print(r+b)
            return
    print(0)

=======
Suggestion 4

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if i == 0:
            continue
        if s[i] != s[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    S = input()
    ans = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == '0':
            count += 1
    print(min(count, len(s) - count) * 2)

=======
Suggestion 7

def main():
    s = input()
    print(min(s.count('0'), s.count('1')) * 2)

=======
Suggestion 8

def main():
    # input
    S = input()

    # compute
    cnt = 0
    for i in range(len(S)-1):
        if S[i] != S[i+1]:
            cnt += 1

    # output
    print(cnt)

=======
Suggestion 9

def main():
    S = input()
    #print(S)
    count = 0
    while True:
        if S.find("01") == -1 and S.find("10") == -1:
            break
        if S.find("01") != -1:
            S = S.replace("01","",1)
            count += 1
        if S.find("10") != -1:
            S = S.replace("10","",1)
            count += 1
    print(count)
main()
