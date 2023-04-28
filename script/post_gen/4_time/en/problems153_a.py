Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    H, A = map(int, input().split())
    if H % A == 0:
        print(int(H / A))
    else:
        print(int(H / A) + 1)

=======
Suggestion 2

def main():
    h,a = map(int,input().split())
    if h%a == 0:
        print(int(h/a))
    else:
        print(int(h/a)+1)

=======
Suggestion 3

def main():
    H, A = map(int, input().split())
    print((H + A - 1) // A)

=======
Suggestion 4

def main():
    h, a = map(int, input().split())
    print((h + a - 1) // a)

=======
Suggestion 5

def main():
    H, A = map(int, input().split())
    print(H//A if H%A==0 else H//A+1)

=======
Suggestion 6

def main():
    H, A = map(int, input().split())
    print((H-1)//A + 1)

=======
Suggestion 7

def main():
    H, A = map(int, input().split())
    print(int((H + A - 1) / A))

=======
Suggestion 8

def solve(H, A):
    num = 0
    while H > 0:
        H -= A
        num += 1
    return num

=======
Suggestion 9

def monster():
    h, a = map(int, input().split())
    return (h + a - 1) // a

print(monster())

=======
Suggestion 10

def solve():
    H,A = map(int,input().split())
    print((H+A-1)//A)
