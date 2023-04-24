Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    print(2 * a + 100 - b)

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a*2+100 >= b:
        print(a*2+100-b)
    else:
        print(0)

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print(2*A+100-B)

=======
Suggestion 4

def main():
    a,b = map(int,input().split())
    if a*2+100 <= b:
        print(0)
    else:
        print(a*2+100-b)

=======
Suggestion 5

def main():
    a, b = [int(x) for x in input().split()]
    print(2 * a + 100 - b)

=======
Suggestion 6

def calc_follow(a,b):
    if b <= 2 * a + 100:
        return 2 * a + 100 - b
    else:
        return 0

=======
Suggestion 7

def main():
    a,b = map(int,input().split())
    ans = 2*a+100-b
    print(ans)
