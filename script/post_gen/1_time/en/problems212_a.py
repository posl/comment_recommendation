Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    A, B = map(int, input().split())
    if A > 0 and B == 0:
        print("Gold")
    elif A == 0 and B > 0:
        print("Silver")
    else:
        print("Alloy")

=======
Suggestion 2

def main():
    A, B = map(int, input().split())
    if A > 0 and B == 0:
        print('Gold')
    elif A == 0 and B > 0:
        print('Silver')
    else:
        print('Alloy')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a > 0 and b == 0:
        print('Gold')
    elif a == 0 and b > 0:
        print('Silver')
    else:
        print('Alloy')

=======
Suggestion 4

def main():
    A, B = map(int, input().split())
    if A == 0:
        print("Silver")
    elif B == 0:
        print("Gold")
    else:
        print("Alloy")

=======
Suggestion 5

def main():
    A, B = map(int, raw_input().split())
    if A > 0 and B == 0:
        print "Gold"
    elif A == 0 and B > 0:
        print "Silver"
    else:
        print "Alloy"

=======
Suggestion 6

def main():
    A, B = input().split()
    if int(A) > 0 and int(B) == 0:
        print("Gold")
    elif int(A) == 0 and int(B) > 0:
        print("Silver")
    elif int(A) > 0 and int(B) > 0:
        print("Alloy")

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if 0 < a and b == 0:
        print('Gold')
    elif a == 0 and 0 < b:
        print('Silver')
    else:
        print('Alloy')

main()

=======
Suggestion 8

def main():
    #get input
    A, B = map(int, input().split())
    #check conditions
    if A > 0 and B == 0:
        print('Gold')
    elif A == 0 and B > 0:
        print('Silver')
    else:
        print('Alloy')
