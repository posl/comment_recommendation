Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    cards = list(map(int, input().split()))
    cards.sort()
    if cards[0] == cards[1] and cards[1] == cards[2] and cards[3] == cards[4]:
        print("Yes")
    elif cards[0] == cards[1] and cards[2] == cards[3] and cards[3] == cards[4]:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 2

def main():
    a,b,c,d,e = map(int,input().split())
    if (a == b == c and d == e) or (a == b and c == d == e):
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a, b, c, d, e = map(int, input().split())
    if (a == b and b == c and d == e and a != d) or (a == b and c == d and d == e and a != c):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    # Enter your code here. Read input from STDIN. Print output to STDOUT
    A, B, C, D, E = map(int, input().split())
    if (A == B == C) and (D == E) or (A == B) and (C == D == E):
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a = input().split()
    a = [int(i) for i in a]
    if len(set(a)) == 2:
        if max(a.count(i) for i in set(a)) == 3:
            print('Yes')
        else:
            print('No')
    else:
        print('No')

=======
Suggestion 6

def main():
    #input
    a,b,c,d,e=map(int,input().split())
    #output
    print("Yes" if (a==b==c and d==e and a!=d) or (a==b and c==d==e and a!=c) else "No")

=======
Suggestion 7

def main():
    # Read input
    A, B, C, D, E = map(int, input().split())

    # Check if the set is a Full house
    if A == B and B == C and D == E:
        print("Yes")
    elif A == B and C == D and D == E:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # Read the input
    A, B, C, D, E = map(int, input().split())
    # Check the conditions
    if (A == B == C and D == E and A != D) or (A == B and C == D == E and A != C):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    # read in the cards
    cards = list(map(int, input().split()))
    # sort the cards
    cards.sort()
    # check if the cards are a full house
    if cards[0] == cards[1] and cards[1] == cards[2] and cards[3] == cards[4]:
        print("Yes")
    elif cards[0] == cards[1] and cards[2] == cards[3] and cards[3] == cards[4]:
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 10

def main():
    # get input
    A, B, C, D, E = map(int, input().split())
    # sort input
    numbers = sorted([A, B, C, D, E])
    # check for full house
    if numbers[0] == numbers[1] == numbers[2] != numbers[3] != numbers[4]:
        if numbers[3] == numbers[4]:
            print('Yes')
            return
    if numbers[0] != numbers[1] != numbers[2] == numbers[3] == numbers[4]:
        if numbers[0] == numbers[1]:
            print('Yes')
            return
    print('No')
