Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    ans = 0
    for i in range(len(s) - 1):
        if s[i] == 'v' and s[i + 1] == 'v':
            ans += 1
        elif s[i] == 'w' and s[i + 1] == 'w':
            ans += 1
    print(ans)

=======
Suggestion 2

def main():
    s = input()
    ans = 0
    for i in range(len(s) - 1):
        if s[i] == "v" and s[i + 1] == "v":
            ans += 1
    print(ans)

=======
Suggestion 3

def main():
    s = input()
    count = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'v':
            count += 1
        elif s[i] == 'w' and s[i+1] == 'w':
            count += 1
    print(count)

=======
Suggestion 4

def main():
    s = input()
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'v':
            cnt += 1
        elif s[i] == 'w' and s[i+1] == 'w':
            cnt += 1
    print(cnt)

=======
Suggestion 5

def main():
    S = input()
    ans = 0
    for i in range(len(S)-1):
        if S[i] == "v" and S[i+1] == "v":
            ans += 1
        elif S[i] == "w" and S[i+1] == "w":
            ans += 1
    print(ans)

=======
Suggestion 6

def main():
    S = input()
    v = 0
    w = 0
    for s in S:
        if s == 'v':
            v += 1
        else:
            w += v
    print(w)

=======
Suggestion 7

def main():
    s = input()
    #print(s)
    cnt = 0
    for i in range(len(s)-1):
        if s[i] == "v" and s[i+1] == "v":
            cnt += 1
        elif s[i] == "w" and s[i+1] == "w":
            cnt += 1
    print(cnt)

main()

=======
Suggestion 8

def main():
    s = input()
    print(s.count("vv") * s.count("w"))
