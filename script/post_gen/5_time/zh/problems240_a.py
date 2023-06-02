Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a,b = map(int, input().split())
    if abs(a-b) == 1 or abs(a-b) == 9:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    a,b = map(int, input().split())
    if a == 1 or a == 3 or a == 5 or a == 7 or a == 9:
        if b == 1 or b == 3 or b == 5 or b == 7 or b == 9:
            print('Yes')
        else:
            print('No')
    else:
        if b == 2 or b == 4 or b == 6 or b == 8 or b == 10:
            print('Yes')
        else:
            print('No')

=======
Suggestion 3

def solve():
    a, b = map(int, input().split())
    if b - a == 1 or b - a == 9:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if b - a == 1 or b - a == 9:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def isConnect(a,b):
    #print(a,b)
    if a==b:
        return True
    if a==1 and b==2:
        return True
    if a==1 and b==3:
        return True
    if a==1 and b==4:
        return True
    if a==1 and b==5:
        return True
    if a==2 and b==3:
        return True
    if a==2 and b==4:
        return True
    if a==2 and b==5:
        return True
    if a==3 and b==4:
        return True
    if a==3 and b==5:
        return True
    if a==4 and b==5:
        return True
    return False

=======
Suggestion 6

def main():
    a,b = map(int, input().split())
    if a+1 == b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a == 4 and b == 5:
        print("Yes")
    elif a == 3 and b == 5:
        print("No")
    elif a == 1 and b == 10:
        print("Yes")

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if a+1 == b or a-1 == b:
        print('Yes')
    else:
        print('No')
