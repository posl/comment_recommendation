Synthesizing 10/10 solutions

=======
Suggestion 1

def getStr(str, begin, end):
    return str[begin-1:end]

str = 'atcoder'
begin, end = map(int, input().split())
print(getStr(str, begin, end))

=======
Suggestion 2

def main():
    L,R = map(int,input().split())
    str = "atcoder"
    print(str[L-1:R])

=======
Suggestion 3

def main():
    s = 'atcoder'
    l, r = map(int, input().split())
    print(s[l-1:r])

=======
Suggestion 4

def main():
    l,r = input().split()
    l = int(l)
    r = int(r)
    atcoder = "atcoder"
    print(atcoder[l-1:r])

=======
Suggestion 5

def getStr(str, start, end):
    return str[start-1:end]

str = "atcoder"
start, end = map(int, input().split())
print(getStr(str, start, end))

=======
Suggestion 6

def main():
    l,r = input().split()
    l = int(l)
    r = int(r)
    s = "atcoder"
    print(s[l-1:r])

=======
Suggestion 7

def getStr(s, start, end):
    return s[start-1:end]

s = input()
l, r = map(int, input().split())
print(getStr(s, l, r))

=======
Suggestion 8

def main():
    L,R = map(int, input().split())
    s = "atcoder"
    print(s[L-1:R])

=======
Suggestion 9

def main():
    line = input()
    l,r = line.split()
    l = int(l)
    r = int(r)
    atcoder = 'atcoder'
    print(atcoder[l-1:r])

=======
Suggestion 10

def main():
    L,R = map(int, input().split())
    str = 'atcoder'
    print(str[L-1:R])
