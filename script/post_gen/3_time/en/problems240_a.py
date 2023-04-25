Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if abs(a - b) == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a + 1 == b or a - 1 == b or a == 1 and b == 10 or a == 10 and b == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if abs(a-b) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a == 1 or b == 1 or abs(a - b) == 1:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a + 1 == b or a - 1 == b or a + 9 == b or a - 9 == b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a, b = map(int,input().split())
    if a in [1,9,7,4] and b in [1,9,7,4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    a,b=map(int,input().split())
    if a == 1 or b == 1 or a == 9 or b == 9:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if (a + 1) % 10 == b % 10:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    a, b = map(int, input().split())
    if (b - a) in [1, 9]:
        print("Yes")
    else:
        print("No")
    
main()

=======
Suggestion 10

def main():
    a,b = map(int, input().split())
    if a == 1 or b == 1 or (a == 9 or b == 9):
        print("Yes")
    else:
        print("No")
