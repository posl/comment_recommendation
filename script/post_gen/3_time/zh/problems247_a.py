Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    print(S[1:]+S[0])
main()

=======
Suggestion 2

def main():
    S = input()
    print(S[1:]+S[0])

=======
Suggestion 3

def problem247_a(s):
    l = list(s)
    l.append('0')
    l.pop(0)
    return "".join(l)

=======
Suggestion 4

def problem247_a():
    s = input()
    print(s[1:] + s[0])

problem247_a()

=======
Suggestion 5

def main():
    s = input()
    print(s[1:]+s[0])

=======
Suggestion 6

def problems247_a():
    s = input()
    print(s[1:] + s[:1])

=======
Suggestion 7

def move(x):
    if x == '1':
        return '0'
    else:
        return '1'

s = input()
ans = ''
for i in s:
    ans += move(i)

print(ans)
