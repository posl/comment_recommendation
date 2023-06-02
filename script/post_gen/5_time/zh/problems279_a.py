Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == "w":
            count += i
    print(count)

=======
Suggestion 2

def count_vw(s):
    count = 0
    for i in range(len(s)):
        if s[i] == "v":
            for j in range(i+1, len(s)):
                if s[j] == "w":
                    count += 1
                else:
                    break
    return count

=======
Suggestion 3

def main():
    s = input()
    print(s.count("wv") + s.count("vw"))

=======
Suggestion 4

def count_bottoms(S):
    count = 0
    for i in range(len(S)):
        if S[i] == 'w':
            count += S.count('v', i + 1)
    return count

S = input()
print(count_bottoms(S))

=======
Suggestion 5

def count_bottom(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            count += s[i+1:].count('v')
    return count

=======
Suggestion 6

def main():
    s = input()
    print(s.count("wv"))

=======
Suggestion 7

def count_underline(S):
    return S.count("vw") + S.count("wv")

=======
Suggestion 8

def main():
    s = input()
    print(s.count('vv'))

=======
Suggestion 9

def count_d(S):
    count = 0
    for i in range(len(S)):
        if S[i] == "v":
            for j in range(i+1, len(S)):
                if S[j] == "w":
                    count += 1
    return count

=======
Suggestion 10

def problems279_a():
    print(input().count('vv'))
