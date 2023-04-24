Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    x = int(input())
    if x == 0:
        print('No')
    elif x % 100 == 0:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    x = int(input())
    if x % 100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    X = int(input())
    if (X % 100 == 0):
        print("Yes")
    else:
        print("No")

main()

=======
Suggestion 4

def main():
    x = int(input())
    y = x % 100
    if y == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def purse(x):
    if x % 100 == 0 and x != 0:
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 6

def main():
    # input
    X = int(input())

    # compute
    if X%100 == 0 and X != 0:
        ans = "Yes"
    else:
        ans = "No"

    # output
    print(ans)

=======
Suggestion 7

def purse(x):
    if x % 100 == 0:
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 8

def main():
    #input
    X = int(input())
    
    #output
    if X % 100 == 0:
        print("Yes")
    else:
        print("No")
    
    return 0

=======
Suggestion 9

def main():
    #write your code here
    x = int(input())
    if x%100 == 0:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def main():
    #read input
    X = int(input())
    #check if X is divisible by 100
    if X % 100 == 0:
        print('Yes')
    else:
        print('No')
