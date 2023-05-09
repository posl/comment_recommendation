Synthesizing 10/10 solutions

=======
Suggestion 1

def full_house(a, b, c, d, e):
    if a == b == c and d == e:
        print("Yes")
    elif a == b and c == d == e:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b, c, d, e = map(int, input().split())
    if a == b and a == c and d == e:
        print('Yes')
    elif a == b and a == d and c == e:
        print('Yes')
    elif a == b and a == e and c == d:
        print('Yes')
    elif a == c and a == d and b == e:
        print('Yes')
    elif a == c and a == e and b == d:
        print('Yes')
    elif a == d and a == e and b == c:
        print('Yes')
    elif b == c and b == d and a == e:
        print('Yes')
    elif b == c and b == e and a == d:
        print('Yes')
    elif b == d and b == e and a == c:
        print('Yes')
    elif c == d and c == e and a == b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    cards = list(map(int, input().split()))
    cards.sort()

    if cards[0] == cards[1] and cards[1] != cards[2] and cards[2] == cards[3] and cards[3] == cards[4]:
        print("Yes")
    elif cards[0] == cards[1] and cards[1] == cards[2] and cards[2] != cards[3] and cards[3] == cards[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    cards = list(map(int, input().split()))
    if cards.count(cards[0]) == 3 or cards.count(cards[0]) == 2:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def solve():
    A, B, C, D, E = map(int, input().split())
    if A == B and B == C and D == E:
        print('Yes')
    elif A == B and C == D and D == E:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def main():
    a,b,c,d,e = map(int, input().split())
    if (a == b and c == d == e) or (a == c and b == d == e) or (a == d and b == c == e) or (a == e and b == c == d) or (b == c and a == d == e) or (b == d and a == c == e) or (b == e and a == c == d) or (c == d and a == b == e) or (c == e and a == b == d) or (d == e and a == b == c):
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def is_full_house(cards):
    cards.sort()
    if cards[0] == cards[1] and cards[2] == cards[3] and cards[3] == cards[4]:
        return True
    elif cards[0] == cards[1] and cards[1] == cards[2] and cards[3] == cards[4]:
        return True
    else:
        return False

cards = list(map(int, input().split()))

=======
Suggestion 8

def main():
    # input
    A, B, C, D, E = map(int, input().split())

    # compute

    # output
    if (A==B and C==D) or (A==B and C==E) or (A==B and D==E) or (A==C and B==D) or (A==C and B==E) or (A==C and D==E) or (A==D and B==C) or (A==D and B==E) or (A==D and C==E) or (A==E and B==C) or (A==E and B==D) or (A==E and C==D) or (B==C and A==D) or (B==C and A==E) or (B==C and D==E) or (B==D and A==C) or (B==D and A==E) or (B==D and C==E) or (B==E and A==C) or (B==E and A==D) or (B==E and C==D) or (C==D and A==B) or (C==D and A==E) or (C==D and B==E) or (C==E and A==B) or (C==E and A==D) or (C==E and B==D) or (D==E and A==B) or (D==E and A==C) or (D==E and B==C):
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    a,b,c,d,e = map(int, input().split())
    if (a == b and c == d and c == e) or (a == b and a == c and d == e):
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    #input_string = input()
    #input_string = "1 2 1 2 1"
    input_string = "12 12 11 1 2"
    input_string = input_string.split()
    input_string = [int(i) for i in input_string]

    input_string.sort()

    #print(input_string)

    if (input_string[0] == input_string[1] and input_string[0] == input_string[2] and input_string[3] == input_string[4]):
        print("Yes")
    elif (input_string[0] == input_string[1] and input_string[2] == input_string[3] and input_string[2] == input_string[4]):
        print("Yes")
    else:
        print("No")
