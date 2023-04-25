Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x, a = map(int, input().split())
    if x < a:
        print(0)
    else:
        print(10)

=======
Suggestion 2

def main():
    X, A = map(int, input().split())
    if X < A:
        print(0)
    else:
        print(10)

=======
Suggestion 3

def main():
    X, A = input().split()
    if int(X) < int(A):
        print(0)
    else:
        print(10)

=======
Suggestion 4

def main():
    X, A = map(int, input().split())
    print(0 if X < A else 10)

=======
Suggestion 5

def main():
    #X and A are integers between 0 and 9 (inclusive).
    #If X is less than A, print 0; if X is not less than A, print 10.
    inp = input().split()
    X = int(inp[0])
    A = int(inp[1])
    if X < A:
        print(0)
    else:
        print(10)

=======
Suggestion 6

def main():
    # Write code here
    X, A = input().split()
    X = int(X)
    A = int(A)
    if X < A:
        print("0")
    else:
        print("10")

=======
Suggestion 7

def   main ():
     x ,  a   =   map ( int ,  input (). split ())
     if  x < a:
         print ( 0 )

=======
Suggestion 8

def main():
    # Get input
    X, A = map(int, input().split())
    # Print output
    print(0 if X < A else 10)
