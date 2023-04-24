Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    s = input()
    if s[0] == s[1] and s[1] == s[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 2

def main():
    c = input()
    if c[0] == c[1] and c[1] == c[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 3

def main():
    s = input()
    if s[0] == s[1] and s[0] == s[2]:
        print('Won')
    else:
        print('Lost')

=======
Suggestion 4

def main():
    c1, c2, c3 = input().split()
    if c1 == c2 and c2 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 5

def main():
    str = input()
    if str[0] == str[1] and str[0] == str[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 6

def main():
    c1, c2, c3 = input().rstrip().split()
    if c1 == c2 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 7

def main():
    c1,c2,c3 = input().strip()
    if c1 == c2 and c2 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 8

def main():
    c = list(input())
    if c[0]==c[1] and c[1]==c[2]:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 9

def main():
    c1,c2,c3 = input().rstrip().split()
    if c1 == c2 and c1 == c3:
        print("Won")
    else:
        print("Lost")

=======
Suggestion 10

def solve():
    a,b,c = map(str, input().split())
    if a==b and b==c:
        print("Won")
    else:
        print("Lost")
