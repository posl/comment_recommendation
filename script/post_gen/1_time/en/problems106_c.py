Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    K = int(input())
    for i in range(K):
        if S[i] != '1':
            print(S[i])
            break
    else:
        print(1)

=======
Suggestion 2

def main():
    s = input()
    k = int(input())
    for i in range(k):
        if s[i] != '1':
            print(s[i])
            return
    print(1)

=======
Suggestion 3

def main():
    S = input()
    K = int(input())
    S = S.replace("1", "1")
    S = S.replace("2", "22")
    S = S.replace("3", "333")
    S = S.replace("4", "4444")
    S = S.replace("5", "55555")
    S = S.replace("6", "666666")
    S = S.replace("7", "7777777")
    S = S.replace("8", "88888888")
    S = S.replace("9", "999999999")
    print(S[K - 1])

=======
Suggestion 4

def main():
    S = input()
    K = int(input())
    s = 0
    for i in range(len(S)):
        if S[i] == '1':
            s += 1
        else:
            break
    if K <= s:
        print(1)
    else:
        print(S[s])

=======
Suggestion 5

def main():
    s = input()
    k = int(input())
    if k <= len(s):
        print(s[k-1])
        return
    i = 0
    while i < len(s) and s[i] == '1':
        i += 1
    if i == len(s):
        print(1)
        return
    if s[i] == '2':
        print(2)
        return
    if s[i] == '3':
        print(3)
        return
    if s[i] == '4':
        print(4)
        return
    if s[i] == '5':
        print(5)
        return
    if s[i] == '6':
        print(6)
        return
    if s[i] == '7':
        print(7)
        return
    if s[i] == '8':
        print(8)
        return
    if s[i] == '9':
        print(9)
        return

=======
Suggestion 6

def main():
    S = input()
    K = int(input())
    ans = ""
    for i in range(len(S)):
        if S[i] == "1":
            ans += "1"
        else:
            ans += "1" * (int(S[i]) - 1)
        if len(ans) >= K:
            break
    print(ans[K - 1])

main()

=======
Suggestion 7

def get_next(s):
    next_s = []
    for c in s:
        if c == '1':
            next_s.append('1')
        else:
            next_s.append(c * int(c))
    return ''.join(next_s)

=======
Suggestion 8

def main():
    S = input()
    K = int(input())
    ans = S[K-1]
    print(ans)

=======
Suggestion 9

def findChar(s, k):
    if k <= len(s):
        return s[k - 1]
    else:
        k -= len(s)
        for i in range(9, 1, -1):
            if k <= i * len(s):
                return s[(k - 1) // i]
            else:
                k -= i * len(s)

s = input()
k = int(input())
print(findChar(s, k))

=======
Suggestion 10

def getstr():
    return input().strip()
