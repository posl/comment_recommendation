Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    ans = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    count = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            count += 1
    print(count)

=======
Suggestion 3

def main():
    n = int(input())
    s = input()
    cnt = 1
    for i in range(n-1):
        if s[i] != s[i+1]:
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            ans += 1
    print(ans)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    ans = 0
    prev = ''
    for i in range(N):
        if prev != S[i]:
            ans += 1
        prev = S[i]
    print(ans)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    ans = 1
    for i in range(1, N):
        if S[i] != S[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 7

def main():
    N = int(input())
    S = input()
    #print(N)
    #print(S)
    slimes = []
    for i in range(N):
        slimes.append(S[i])
    #print(slimes)
    i = 0
    while(i < len(slimes)-1):
        if slimes[i] == slimes[i+1]:
            slimes.pop(i+1)
            i = i-1
        else:
            i = i+1
    print(len(slimes))
