Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    N = int(input())
    S = input()
    if N == 1:
        print(1)
        return
    slime = []
    for i in range(N):
        if i == 0:
            slime.append(S[i])
        elif slime[-1] != S[i]:
            slime.append(S[i])
    print(len(slime))

=======
Suggestion 2

def main():
    n = int(input())
    s = input()
    ans = 1
    for i in range(1,n):
        if s[i] != s[i-1]:
            ans += 1
    print(ans)

=======
Suggestion 3

def solve():
    n = int(input())
    s = input()
    count = 1
    for i in range(1, n):
        if s[i] != s[i-1]:
            count += 1
    print(count)

=======
Suggestion 4

def main():
    # 读取输入
    N = int(input())
    S = input()
    # print('N=', N)
    # print('S=', S)
    # 统计粘液数量
    slime_count = 1
    for i in range(1, N):
        if S[i] != S[i-1]:
            slime_count += 1
    # 输出结果
    print(slime_count)

=======
Suggestion 5

def main():
    N = int(input())
    S = input()
    cnt = 1
    for i in range(1, N):
        if S[i] != S[i-1]:
            cnt += 1
    print(cnt)

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    if N == 1:
        print(1)
        return
    slime = []
    for i in range(N):
        slime.append(S[i])
    i = 0
    while i < len(slime)-1:
        if slime[i] == slime[i+1]:
            del slime[i+1]
        else:
            i += 1
    print(len(slime))
main()

=======
Suggestion 7

def mergeSlime(slime):
    #merge
    i = 0
    while i < len(slime) - 1:
        if slime[i] == slime[i + 1]:
            slime[i] = slime[i] + slime[i + 1]
            slime.pop(i + 1)
        else:
            i += 1
    #print(slime)
    #merge again
    i = 0
    while i < len(slime) - 1:
        if slime[i][-1] == slime[i + 1][0]:
            slime[i] = slime[i] + slime[i + 1]
            slime.pop(i + 1)
        else:
            i += 1
    #print(slime)
    return slime

=======
Suggestion 8

def slime(s):
    if len(s) == 1:
        return 1
    else:
        i = 0
        while i < len(s):
            if i == len(s) - 1:
                break
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                i = 0
            else:
                i += 1
        return len(s)

=======
Suggestion 9

def main():
    N = int(input())
    S = input()
    count = 1
    for i in range(N-1):
        if S[i] != S[i+1]:
            count += 1
    print(count)

=======
Suggestion 10

def solution():
    N = int(input())
    S = input()
    cnt = 1
    for i in range(1, N):
        if S[i-1] != S[i]:
            cnt += 1
    print(cnt)
solution()
