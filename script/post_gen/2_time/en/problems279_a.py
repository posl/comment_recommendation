Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    S = input()
    count = 0
    for i in range(len(S)-1):
        if S[i] == 'v' and S[i+1] == 'w':
            count += 1
    print(count)

=======
Suggestion 2

def main():
    s = input()
    v = 0
    w = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 'v':
            v += 1
        else:
            w += 1
            ans += v
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            for j in range(i+1, len(s)):
                if s[j] == 'v':
                    count += 1
    print(count)

=======
Suggestion 4

def main():
    s = input()
    v = 0
    w = 0
    count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            v += 1
        else:
            w += 1
        if v > w:
            count += 1
    print(count)

=======
Suggestion 5

def main():
    s = input()
    v = 0
    w = 0
    count = 0
    for i in s:
        if i == 'v':
            v += 1
        elif i == 'w':
            w += 1
        if v == w and v > 0:
            count += 1
    print(count)

=======
Suggestion 6

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            count += 1
    print(count * (count - 1) // 2)

=======
Suggestion 7

def main():
    s = input()
    ans = 0
    for i in range(len(s)):
        if s[i] == 'v' and i+1 < len(s) and s[i+1] == 'v':
            ans += 1
    print(ans)

=======
Suggestion 8

def main():
    s = input()
    #print(s)
    v = 0
    w = 0
    for i in range(len(s)):
        if s[i] == 'v':
            v += 1
        else:
            w += 1
    #print(v, w)
    print(v * w)

=======
Suggestion 9

def main():
    S = input()
    if S[0] == 'v':
        print(len(S) - 1)
    else:
        print(len(S))

=======
Suggestion 10

def bottoms(s):
    return (s.count('v') + 1) * s.count('w')
