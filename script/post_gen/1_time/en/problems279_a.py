Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    n = 0
    for i in range(len(s)-1):
        if s[i] == 'v' and s[i+1] == 'v':
            n += 1
    print(n)

=======
Suggestion 2

def main():
    S = input()
    bottoms = 0
    for i in range(len(S)-1):
        if S[i] == 'v' and S[i+1] == 'v':
            bottoms += 1
    print(bottoms)

=======
Suggestion 3

def main():
    s = input()
    v = 0
    w = 0
    ans = 0
    for i in range(len(s)):
        if s[i] == 'v':
            v += 1
        if s[i] == 'w':
            w += 1
        if v > w:
            ans += 1
    print(ans)

=======
Suggestion 4

def main():
    S = input()
    count = 0
    for i in range(len(S)):
        if S[i] == "v":
            count += 1
    print(count * (count - 1) // 2)

=======
Suggestion 5

def main():
    S = input()
    count = 0
    bottom = 0
    for i in S:
        if i == 'v':
            count += 1
            if count == 1:
                bottom += 1
        else:
            count -= 1
    print(bottom)

=======
Suggestion 6

def main():
    s = input()
    print(s.count('v') * (s.count('v') - 1) // 2)

=======
Suggestion 7

def main():
    s = input()
    v = s.count("v")
    w = s.count("w")
    print(v * w)

main()

=======
Suggestion 8

def main():
    s = input()
    print(s.count('v')*s.count('w'))

=======
Suggestion 9

def main():
    S = input()
    print(S.count('v') * S.count('w'))
