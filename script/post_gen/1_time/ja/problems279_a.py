Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'w':
            count += 1
    print(count*2)

=======
Suggestion 2

def main():
    S = input()
    ans = 0
    for i in range(len(S)-1):
        if S[i] == "v" and S[i+1] == "w":
            ans += 1
    print(ans*2)

=======
Suggestion 3

def main():
    s = input()
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == "v" and s[i+1] == "w":
            cnt += 1
        elif s[i] == "w" and s[i+1] == "v":
            cnt += 1
    print(cnt)

=======
Suggestion 4

def main():
    s = input()
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == 'v':
            if s[i+1] == 'v':
                cnt += 1
            else:
                cnt += 2
    print(cnt)

=======
Suggestion 5

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == "v" and i+1 < len(s) and s[i+1] == "v":
            count += 1
    print(count * (count-1) // 2)

=======
Suggestion 6

def main():
    s = input()
    v = 0
    w = 0
    count = 0
    for i in range(len(s)):
        if s[i] == "v":
            v += 1
        else:
            w += 1
        if v > w:
            count += 1
    print(count)

=======
Suggestion 7

def main():
    S = input()
    v = 0
    w = 0
    for s in S:
        if s == "v":
            v += 1
        else:
            w += 1
    print(v * w)

=======
Suggestion 8

def main():
    s = input()
    v = s.count("v")
    w = s.count("w")
    print(v*w)

=======
Suggestion 9

def main():
    s = input()
    print(s.count("vv"))

=======
Suggestion 10

def main():
    S = input()
    print(S.count("v") * S.count("w"))
