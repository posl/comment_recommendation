Synthesizing 10/10 solutions

=======
Suggestion 1

def isFullHouse(a, b, c, d, e):
    if a == b and b == c and d == e:
        return True
    elif a == b and c == d and d == e:
        return True
    else:
        return False

=======
Suggestion 2

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] and a[2] == a[3] == a[4]:
        print('Yes')
    elif a[0] == a[1] == a[2] and a[3] == a[4]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    a,b,c,d,e = map(int, input().split())
    if (a == b and b == c and d == e) or (a == b and c == d and d == e):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    a,b,c,d,e = map(int, input().split())
    if a==b==c and d==e:
        print("Yes")
    elif a==b==d and c==e:
        print("Yes")
    elif a==b==e and c==d:
        print("Yes")
    elif a==c==d and b==e:
        print("Yes")
    elif a==c==e and b==d:
        print("Yes")
    elif a==d==e and b==c:
        print("Yes")
    elif b==c==d and a==e:
        print("Yes")
    elif b==c==e and a==d:
        print("Yes")
    elif b==d==e and a==c:
        print("Yes")
    elif c==d==e and a==b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    cards = input().split()
    cards.sort()
    if cards[0] == cards[1] and cards[2] == cards[3] and cards[3] == cards[4]:
        print("No")
    elif cards[0] == cards[1] and cards[1] == cards[2] and cards[3] == cards[4]:
        print("No")
    else:
        print("Yes")

=======
Suggestion 6

def main():
    cards = list(map(int, input().split()))
    cards.sort()
    if cards[0]==cards[1] and cards[1]==cards[2] and cards[3]==cards[4]:
        print('Yes')
    elif cards[0]==cards[1] and cards[2]==cards[3] and cards[3]==cards[4]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    a = input().split()
    if (a[0] == a[1] and a[2] == a[3] and a[3] == a[4]) or (a[0] == a[1] and a[1] == a[2] and a[3] == a[4]):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a,b,c,d,e = map(int,input().split())
    if a == b and c == d and d == e:
        print("Yes")
    elif a == c and b == d and d == e:
        print("Yes")
    elif a == d and b == c and c == e:
        print("Yes")
    elif a == e and b == c and c == d:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def checkFullHouse():
    input = raw_input().split()
    input.sort()
    if (input[0] == input[1] and input[3] == input[4] and (input[2] == input[1] or input[2] == input[3])):
        print "Yes"
    else:
        print "No"

checkFullHouse()

=======
Suggestion 10

def checkFullHouse(input):
    input = input.split()
    input.sort()
    if ((input[0] == input[1]) and (input[1] != input[2]) and (input[2] == input[3]) and (input[3] == input[4])):
        print("Yes")
    elif ((input[0] == input[1]) and (input[1] == input[2]) and (input[2] != input[3]) and (input[3] == input[4])):
        print("Yes")
    else:
        print("No")

input = input()
checkFullHouse(input)
