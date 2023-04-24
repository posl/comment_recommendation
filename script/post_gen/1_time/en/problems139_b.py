Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if B % A == 0:
        print(B // A)
    else:
        print(B // A + 1)

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    print((B + A - 3) // (A - 1))

=======
Suggestion 3

def main():
    A, B = map(int, input().split())
    print((B - 1) // (A - 1))

=======
Suggestion 4

def main():
    #input
    A, B = map(int, input().split())
    #compute
    if B % A == 0:
        ans = B // A
    else:
        ans = B // A + 1
    #output
    print(ans)

=======
Suggestion 5

def main():
    A, B = map(int, input().split())
    print((B-1+A-2)//(A-1))

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    if b%a == 0:
        print(b//a)
    else:
        print(b//a+1)
    return

=======
Suggestion 7

def main():
    #Write code here
    A, B = map(int, input().split())
    count = 1
    while A*count < B:
        count += 1
    print(count)

=======
Suggestion 8

def main():
    a,b = map(int, input().split())
    print((b+a-1)//a)
