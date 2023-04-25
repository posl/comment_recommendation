Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == 'o':
            X += 1
        else:
            if X > 0:
                X -= 1
    print(X)

=======
Suggestion 2

def main():
    N, X = map(int, input().split())
    S = input()
    for i in range(N):
        if S[i] == "o":
            X += 1
        else:
            if X > 0:
                X -= 1
    print(X)

=======
Suggestion 3

def main():
    N, X = map(int, input().split())
    S = input()
    
    for i in range(N):
        if S[i] == 'o':
            X += 1
        else:
            if X > 0:
                X -= 1
    print(X)
    
main()

=======
Suggestion 4

def main():
    n, x = map(int, input().split())
    s = input()
    for i in range(n):
        if s[i] == 'o':
            x += 1
        elif x != 0:
            x -= 1
    print(x)

=======
Suggestion 5

def main():
    n,x = map(int,input().split())
    s = input()
    for i in range(n):
        if s[i] == 'o':
            x += 1
        elif s[i] == 'x' and x > 0:
            x -= 1
    print(x)
main()

=======
Suggestion 6

def main():
    n, x = map(int, input().split())
    s = list(input())
    for i in range(n):
        if s[i] == 'o':
            x += 1
        else:
            if x > 0:
                x -= 1
    print(x)

main()

=======
Suggestion 7

def main():
    #input
    N, X = map(int, input().split())
    S = input()

    #compute
    for i in range(N):
        if S[i] == 'o':
            X += 1
        else:
            if X > 0:
                X -= 1

    #output
    print(X)

=======
Suggestion 8

def main():
    # Read the input
    N, X = map(int, input().split())
    S = input()
    # Solve the problem
    for i in range(N):
        if S[i] == 'o':
            X += 1
        elif S[i] == 'x' and X > 0:
            X -= 1
    # Print the answer
    print(X)
