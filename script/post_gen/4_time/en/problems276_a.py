Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    s = input()
    if 'a' in s:
        print(s.rfind('a')+1)
    else:
        print(-1)

=======
Suggestion 2

def main():
    input_str = input()
    if 'a' in input_str:
        print(input_str.rindex('a') + 1)
    else:
        print(-1)

main()

=======
Suggestion 3

def last_index(s, c):
    if c in s:
        return len(s) - s[::-1].index(c)
    else:
        return -1

=======
Suggestion 4

def main():
    s = input()
    print(s.rfind('a') + 1)

=======
Suggestion 5

def last_index(s):
    for i in range(len(s)):
        if s[i] == 'a':
            index = i+1
    return index

s = input()
print(last_index(s))

=======
Suggestion 6

def main():
    S = input()
    print(S.rfind('a')+1)

=======
Suggestion 7

def main():
    s = input()
    print(s.rfind("a")+1)
