Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a = list(map(int, input().split()))
    a.sort()
    if a[0] == a[1] and a[1] == a[2] and a[3] == a[4]:
        print('Yes')
    elif a[0] == a[1] and a[2] == a[3] and a[3] == a[4]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def is_full_house(a, b, c, d, e):
    if a == b and b == c and d == e:
        return True
    if a == b and c == d and d == e:
        return True
    return False

a, b, c, d, e = map(int, input().split())

=======
Suggestion 3

def main():
    nums = list(map(int, input().split()))
    nums.sort()
    if (nums[0] == nums[1] and nums[1] == nums[2] and nums[3] == nums[4]):
        print('Yes')
    elif (nums[0] == nums[1] and nums[2] == nums[3] and nums[3] == nums[4]):
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    A,B,C,D,E = map(int,input().split())
    if A == B == C and D != E:
        print('Yes')
    elif D == E == C and A != B:
        print('Yes')
    elif A == B == D and C != E:
        print('Yes')
    elif A == B == E and C != D:
        print('Yes')
    elif A == C == D and B != E:
        print('Yes')
    elif A == C == E and B != D:
        print('Yes')
    elif A == D == E and B != C:
        print('Yes')
    elif B == C == D and A != E:
        print('Yes')
    elif B == C == E and A != D:
        print('Yes')
    elif B == D == E and A != C:
        print('Yes')
    elif C == D == E and A != B:
        print('Yes')
    else:
        print('No')

=======
Suggestion 5

def main():
    # A,B,C,D,E = input().split()
    # A,B,C,D,E = int(A),int(B),int(C),int(D),int(E)
    A,B,C,D,E = map(int,input().split())
    if A == B == C and D == E and A != D and B != E and C != D:
        print('Yes')
    elif A == B == D and C == E and A != C and B != E and D != C:
        print('Yes')
    elif A == B == E and C == D and A != C and B != D and E != C:
        print('Yes')
    elif A == C == D and B == E and A != B and C != E and D != B:
        print('Yes')
    elif A == C == E and B == D and A != B and C != D and E != B:
        print('Yes')
    elif A == D == E and B == C and A != B and D != C and E != B:
        print('Yes')
    elif B == C == D and A == E and B != A and C != E and D != A:
        print('Yes')
    elif B == C == E and A == D and B != A and C != D and E != A:
        print('Yes')
    elif B == D == E and A == C and B != A and D != C and E != A:
        print('Yes')
    elif C == D == E and A == B and C != A and D != B and E != A:
        print('Yes')
    else:
        print('No')

=======
Suggestion 6

def is_full_house(a, b, c, d, e):
    # write your code here
    return "Yes" if (a == b == c and d == e) or (a == b and c == d == e) else "No"

=======
Suggestion 7

def main():
    #input
    A, B, C, D, E = map(int, input().split())
    #output
    if (A == B == C and D != E) or (A == B == D and C != E) or (A == B == E and C != D) or (A == C == D and B != E) or (A == C == E and B != D) or (A == D == E and B != C) or (B == C == D and A != E) or (B == C == E and A != D) or (B == D == E and A != C) or (C == D == E and A != B):
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    # Put your code here
    a = input().split()
    a = [int(i) for i in a]
    a.sort()
    if a[0] == a[1] == a[2] and a[3] == a[4]:
        print("Yes")
    elif a[0] == a[1] and a[2] == a[3] == a[4]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    # Write your code here
    pass

=======
Suggestion 10

def main():
    # read input
    # split the input into a list of strings
    # convert the list of strings into a list of integers
    # assign each integer to a variable
    a,b,c,d,e = [int(x) for x in input().split()]
    # use a set to get a list of unique values
    # if the length of the set is 2, then there are 3 cards with one value and 2 cards with another value
    if len(set([a,b,c,d,e])) == 2:
        print("Yes")
    else:
        print("No")

main()

This code is a little different from the other solutions. It uses a set to get a list of unique values. If the length of the set is 2, then there are 3 cards with one value and 2 cards with another value.

The code is pretty simple. It reads the input and converts it to a list of integers. It then uses a set to get a list of unique values. If the length of the set is 2, then there are 3 cards with one value and 2 cards with another value. The code then prints Yes o
