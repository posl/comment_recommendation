Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S = input()
    if S.rfind('a') == -1:
        print(-1)
    else:
        print(S.rfind('a')+1)

=======
Suggestion 2

def main():
    S = input()
    if S.find('a') == -1:
        print(-1)
    else:
        print(S.rfind('a')+1)

=======
Suggestion 3

def last_index(str, c):
    for i in range(len(str), 0, -1):
        if str[i-1] == c:
            return i
    return -1

s = input()
print(last_index(s, 'a'))

=======
Suggestion 4

def main():
    s = input()
    a = s.rfind('a')
    print(a+1 if a != -1 else -1)

=======
Suggestion 5

def main():
    s = input()
    print(s.rfind('a') + 1)

=======
Suggestion 6

def lastIndexOfA(s):
    return s.rfind('a') + 1

print(lastIndexOfA(input()))

=======
Suggestion 7

def last_index(s, c):
    return s.rfind(c) + 1
