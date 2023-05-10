Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    print(2*a+100-b)

=======
Suggestion 2

def main():
    a, b = map(int, input().strip().split())
    print(2 * a + 100 - b)

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    print((2*a)+100-b)

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    print(2*A+100-B)

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    
    if b <= 2*a+100:
        print(2*a+100-b)
    else:
        print(0)
