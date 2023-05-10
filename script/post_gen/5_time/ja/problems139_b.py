Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if b % a == 0:
        print(b // a)
    else:
        print(b // a + 1)

=======
Suggestion 2

def main():
    a,b = map(int, input().split())
    print((b-1 + a-2)//(a-1))

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print((B-1)//(A-1))

=======
Suggestion 4

def main():
    a, b = map(int, input().split())

    if b == 1:
        print(0)
    else:
        if b % (a-1) == 0:
            print(b // (a-1))
        else:
            print(b // (a-1) + 1)

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    if b % a == 0:
        print(b // a)
    else:
        print((b // a) + 1)

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if b % a == 0:
        print(int(b/a)-1)
    else:
        print(int(b/a))

=======
Suggestion 7

def main():
    A, B = map(int, input().split())
    ans = 0
    while B > 1:
        B -= A - 1
        ans += 1
    print(ans)

=======
Suggestion 8

def calc(a,b):
    if b == 1:
        return 0
    else:
        return int((b-1)/(a-1))+1
