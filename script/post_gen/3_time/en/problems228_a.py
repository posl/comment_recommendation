Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    S, T, X = map(int, input().split())
    if S <= X and X < T:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    s, t, x = map(int, input().split())
    if s <= x and x < t:
        print("Yes")
    elif t < s and (x < t or s <= x):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    S, T, X = map(int, input().split())
    if S <= X and X < T:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    S, T, X = map(int, input().split())
    if S <= X < T:
        print('Yes')
    elif S > T and (X < T or S <= X):
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 5

def main():
    S, T, X = map(int, input().split())
    if (S <= X and X < T) or (S <= X + 24 and X + 24 < T):
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    s, t, x = map(int, input().split())
    if s <= x <= t:
        print("Yes")
    elif t < s and (x >= s or x <= t):
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    S, T, X = map(int, input().split())
    if X >= S and X+1 <= T:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 8

def main():
    S,T,X = [int(x) for x in input().split()]
    if S <= X and X < T:
        print('Yes')
    elif S > T and (X >= S or X < T):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    s,t,x = map(int, input().split())
    if s <= x:
        if x < t:
            print("Yes")
        elif s < t:
            print("No")
        else:
            if x == s:
                print("Yes")
            else:
                print("No")
    else:
        if t < s:
            print("Yes")
        else:
            print("No")
