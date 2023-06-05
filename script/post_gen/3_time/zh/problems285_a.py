Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a < b and a >= 1 and b <= 15:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def solve(a, b):
    if a == 1 and b == 2:
        return True
    if a == 2 and b == 3:
        return True
    if a == 3 and b == 4:
        return True
    if a == 4 and b == 5:
        return True
    if a == 5 and b == 6:
        return True
    if a == 6 and b == 7:
        return True
    if a == 7 and b == 8:
        return True
    if a == 8 and b == 9:
        return True
    if a == 9 and b == 10:
        return True
    if a == 10 and b == 11:
        return True
    if a == 11 and b == 12:
        return True
    if a == 12 and b == 13:
        return True
    if a == 13 and b == 14:
        return True
    if a == 14 and b == 15:
        return True
    return False

=======
Suggestion 3

def main():
    a,b = map(int,input().split())
    if a+b==3 or a+b==7 or a+b==11:
        print("Yes")
    else:
        print("No")

=======
Suggestion 4

def is_connect(a, b):
    if a == 1 and b == 2:
        return True
    elif a == 2 and b == 3:
        return True
    elif a == 3 and b == 4:
        return True
    elif a == 4 and b == 5:
        return True
    elif a == 5 and b == 6:
        return True
    elif a == 6 and b == 7:
        return True
    elif a == 7 and b == 8:
        return True
    elif a == 8 and b == 9:
        return True
    elif a == 9 and b == 10:
        return True
    elif a == 10 and b == 11:
        return True
    elif a == 11 and b == 12:
        return True
    elif a == 12 and b == 13:
        return True
    elif a == 13 and b == 14:
        return True
    elif a == 14 and b == 15:
        return True
    else:
        return False

=======
Suggestion 5

def solve(a, b):
    if (a == 8 and b == 13) or (a == 13 and b == 8):
        return 'Yes'
    elif (a == 1 and b == 15) or (a == 15 and b == 1):
        return 'Yes'
    elif (a == 4 and b == 12) or (a == 12 and b == 4):
        return 'Yes'
    elif (a == 5 and b == 9) or (a == 9 and b == 5):
        return 'Yes'
    else:
        return 'No'

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if abs(a-b)==1 or abs(a-b)==4:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    a,b=map(int,input().split())
    if a==1 and b==2:
        print("Yes")
    elif a==2 and b==3:
        print("Yes")
    elif a==3 and b==4:
        print("Yes")
    elif a==4 and b==5:
        print("Yes")
    elif a==5 and b==6:
        print("Yes")
    elif a==6 and b==7:
        print("Yes")
    elif a==7 and b==8:
        print("Yes")
    elif a==8 and b==9:
        print("Yes")
    elif a==9 and b==10:
        print("Yes")
    elif a==10 and b==11:
        print("Yes")
    elif a==11 and b==12:
        print("Yes")
    elif a==12 and b==13:
        print("Yes")
    elif a==13 and b==14:
        print("Yes")
    elif a==14 and b==15:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a,b = map(int, input().split())
    if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 4) or (a == 4 and b == 5) or (a == 5 and b == 6) or (a == 6 and b == 7) or (a == 7 and b == 8) or (a == 8 and b == 9) or (a == 9 and b == 10) or (a == 10 and b == 11) or (a == 11 and b == 12) or (a == 12 and b == 13) or (a == 13 and b == 14) or (a == 14 and b == 15):
        print("Yes")
    else:
        print("No")

=======
Suggestion 9

def main():
    a,b = map(int, input().split())
    if a == 1 and b == 2:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def isLine(a,b):
    if a>b:
        a,b=b,a
    if a==1 and b==2:
        return True
    if a==2 and b==3:
        return True
    if a==3 and b==4:
        return True
    if a==4 and b==5:
        return True
    if a==5 and b==6:
        return True
    if a==6 and b==7:
        return True
    if a==7 and b==8:
        return True
    if a==8 and b==9:
        return True
    if a==9 and b==10:
        return True
    if a==10 and b==11:
        return True
    if a==11 and b==12:
        return True
    if a==12 and b==13:
        return True
    if a==13 and b==14:
        return True
    if a==14 and b==15:
        return True
    return False
