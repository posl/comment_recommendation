Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    cards = list(map(int,input().split()))
    cards.sort()
    if cards[0] == cards[1] == cards[2] and cards[3] == cards[4]:
        print("Yes")
    elif cards[0] == cards[1] and cards[2] == cards[3] == cards[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    cards = input().split()
    if cards[0] == cards[1] == cards[2]:
        if cards[3] == cards[4]:
            print("Yes")
        else:
            print("No")
    elif cards[0] == cards[1]:
        if cards[2] == cards[3] == cards[4]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

=======
Suggestion 3

def main():
    a = [int(x) for x in input().split()]
    if (a[0] == a[1] == a[2] and a[3] == a[4]) or (a[0] == a[1] and a[2] == a[3] == a[4]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    cards = input().split()
    cards = list(map(int, cards))
    cards.sort()
    if cards[0] == cards[1] and cards[1] == cards[2] and cards[3] == cards[4]:
        print('Yes')
    elif cards[0] == cards[1] and cards[2] == cards[3] and cards[3] == cards[4]:
        print('Yes')
    else:
        print('No')

main()

=======
Suggestion 5

def is_full_house(A,B,C,D,E):
    if A==B and B==C:
        if D==E:
            return True
    if A==B and B==D:
        if C==E:
            return True
    if A==B and B==E:
        if C==D:
            return True
    if A==C and C==D:
        if B==E:
            return True
    if A==C and C==E:
        if B==D:
            return True
    if A==D and D==E:
        if B==C:
            return True
    if B==C and C==D:
        if A==E:
            return True
    if B==C and C==E:
        if A==D:
            return True
    if B==D and D==E:
        if A==C:
            return True
    if C==D and D==E:
        if A==B:
            return True
    return False

A,B,C,D,E = map(int,input().split())

=======
Suggestion 6

def is_full_house(a,b,c,d,e):
    if a == b == c:
        if d == e:
            return True
    if a == b:
        if c == d == e:
            return True
    return False

=======
Suggestion 7

def main():
    #input
    a,b,c,d,e = map(int,input().split())
    #output
    if (a == b == c and d == e) or (a == b and c == d == e):
        print('Yes')
    else:
        print('No')

=======
Suggestion 8

def main():
    #input
    A,B,C,D,E = map(int,input().split())
    #output
    if A == B and B == C and D == E:
        print("Yes")
    elif A == B and C == D and D == E:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    # Read the input
    A, B, C, D, E = map(int, input().split())
    
    # Check if the condition is satisfied
    if A == B == C and D == E:
        print('Yes')
    elif A == B and C == D == E:
        print('Yes')
    else:
        print('No')

=======
Suggestion 10

def main():
    # Read input from stdin
    A,B,C,D,E = map(int,input().split())
    # Check if the set is a Full house
    if A == B == C and D == E:
        print("Yes")
    elif A == B and C == D == E:
        print("Yes")
    else:
        print("No")
