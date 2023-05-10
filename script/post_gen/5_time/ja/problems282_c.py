Synthesizing 10/10 solutions

=======
Suggestion 1

def problems282_c():
    n = int(input())
    s = input()

    cnt = 0
    ans = ''
    for i in range(n):
        if s[i] == '"':
            cnt += 1
        elif s[i] == ',':
            if cnt % 2 == 0:
                ans += ','
            else:
                ans += '.'
        else:
            ans += s[i]

    print(ans)

=======
Suggestion 2

def main():
    N = int(input())
    S = input()
    if N == 2:
        if S[0] == '"':
            print(S[0] + '.' + S[1])
        else:
            print(S[0] + '.' + S[1])
    else:
        for i in range(0, N):
            if S[i] == '"':
                for j in range(i+1, N):
                    if S[j] == '"':
                        for k in range(i+1, j):
                            if S[k] == ',':
                                S = S[:k] + '.' + S[k+1:]
                                break
                        break
        print(S)

=======
Suggestion 3

def main():
    N = int(input())
    S = input()
    cnt = 0
    ans = ""
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        elif cnt%2 == 1 and S[i] == ',':
            ans += '.'
        else:
            ans += S[i]
    print(ans)

=======
Suggestion 4

def main():
    n = int(input())
    s = input()
    s = list(s)
    k = 0
    for i in range(n):
        if s[i] == '"':
            k += 1
        if s[i] == ',' and k % 2 == 0:
            s[i] = '.'
    print(''.join(s))
main()

=======
Suggestion 5

def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in range(n):
        if(s[i] == "\""):
            cnt += 1
        elif(s[i] == "," and cnt % 2 == 1):
            print(".",end="")
        else:
            print(s[i],end="")
    print()
main()

=======
Suggestion 6

def main():
    N = int(input())
    S = input()
    cnt = 0
    for i in range(N):
        if S[i] == '"':
            cnt += 1
        elif S[i] == ',':
            if cnt % 2 == 1:
                S = S[:i] + '.' + S[i+1:]
    print(S)

=======
Suggestion 7

def problems282_c():
    n = int(input())
    s = input()
    res = ""
    cnt = 0
    for i in range(n):
        if s[i] == '"':
            cnt += 1
            if cnt % 2 == 1:
                res += '"'
            else:
                res += '.'
        else:
            res += s[i]
    print(res)

=======
Suggestion 8

def main():
    n = int(input())
    s = input()
    t = ""
    cnt = 0
    for c in s:
        if c == '"':
            cnt += 1
        if cnt % 2 == 1 and c == ',':
            c = '.'
        t += c
    print(t)

=======
Suggestion 9

def main():
    n = int(input())
    s = input()
    cnt = 0
    for c in s:
        if c == '"':
            cnt += 1
    if cnt % 2 != 0:
        print("error")
        return
    cnt //= 2
    ret = ""
    for c in s:
        if c == ',' and cnt > 0:
            c = '.'
            cnt -= 1
        ret += c
    print(ret)

=======
Suggestion 10

def solve():
    n = int(input())
    s = input()
    cnt = 0
    ans = ""
    for i in range(n):
        if s[i] == '"':
            cnt += 1
        elif s[i] == ',':
            if cnt % 2 == 1:
                ans += s[i]
            else:
                ans += '.'
        else:
            ans += s[i]
    print(ans)
