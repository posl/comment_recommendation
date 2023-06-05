Synthesizing 10/10 solutions

=======
Suggestion 1

def count_bottoms(s):
    return s.count("wv") + s.count("vvv")

=======
Suggestion 2

def count_bottoms(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            for j in range(i+1, len(s)):
                if s[j] == 'v':
                    count += 1
    return count

=======
Suggestion 3

def main():
    s = input()
    print(s.count('w'))

=======
Suggestion 4

def main():
    s = input()
    print(s.count('wv'))

=======
Suggestion 5

def count_d(S):
    count = 0
    for i in range(len(S)):
        if S[i] == "w":
            count += S.count("v", i)
    return count

=======
Suggestion 6

def count_bottoms(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            for j in range(i, len(s)):
                if s[j] == 'v':
                    count += 1
                else:
                    break
    return count

=======
Suggestion 7

def problems279_a(S):
    # print(S)
    count = 0
    for i in range(len(S)):
        if S[i] == 'w':
            count += 1
    return count

=======
Suggestion 8

def main():
    s = input()
    print(s.count('wv'))
main()

=======
Suggestion 9

def count_bottom(s):
    count = 0
    for i in range(len(s)):
        if s[i] == 'v':
            count += s[i:].count('w')
    return count

=======
Suggestion 10

def solve():
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] == 'w':
            for j in range(i+1, len(s)):
                if s[j] == 'w':
                    count += 1
    print(count)
