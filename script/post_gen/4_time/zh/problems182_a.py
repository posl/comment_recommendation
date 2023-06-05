Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    print(2*a+100-b)

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    if b <= 2*a + 100:
        print(2*a+100-b)
    else:
        print(0)

=======
Suggestion 3

def solve(a, b):
    if a == 0:
        return 0
    if a == 1:
        return 100
    return 2 * a - b

=======
Suggestion 4

def main():
    a,b = map(int,raw_input().split())
    print 2*a+100-b
