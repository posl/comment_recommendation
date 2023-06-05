Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b = input().split()
    a = int(a)
    b = int(b)
    if b-a == 1 or b-a == -1 or b-a == 9:
        print('Yes')
    else:
        print('No')

=======
Suggestion 2

def main():
    a,b = map(int,input().split())
    if a<b and a>=1 and b<=10:
        print("Yes")
    else:
        print("No")

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if 1 <= a and a <= 10 and 1 <= b and b <= 10:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a == 1 or a == 3 or a == 5 or a == 7 or a == 8 or a == 10:
        if b == 1 or b == 3 or b == 5 or b == 7 or b == 8 or b == 10:
            print("Yes")
        else:
            print("No")
    elif a == 4 or a == 6 or a == 9:
        if b == 4 or b == 6 or b == 9:
            print("Yes")
        else:
            print("No")
    elif a == 2:
        if b == 2:
            print("Yes")
        else:
            print("No")

=======
Suggestion 5

def judge(a,b):
    if a>b:
        a,b=b,a
    if a==1 and b==2:
        print("Yes")
    elif a==2 and b==4:
        print("Yes")
    elif a==3 and b==4:
        print("Yes")
    elif a==3 and b==5:
        print("Yes")
    elif a==4 and b==5:
        print("Yes")
    elif a==5 and b==6:
        print("Yes")
    elif a==6 and b==7:
        print("Yes")
    elif a==6 and b==8:
        print("Yes")
    elif a==7 and b==8:
        print("Yes")
    elif a==7 and b==9:
        print("Yes")
    elif a==8 and b==9:
        print("Yes")
    elif a==8 and b==10:
        print("Yes")
    elif a==9 and b==10:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if a+1 == b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 7

def isConnect(a,b):
    if a == 1 and b == 10:
        return True
    elif a == 2 and b == 9:
        return True
    elif a == 3 and b == 8:
        return True
    elif a == 4 and b == 7:
        return True
    elif a == 5 and b == 6:
        return True
    else:
        return False

=======
Suggestion 8

def problems240_a(a,b):
    if a < b:
        print('Yes')
    else:
        print('No')

problems240_a(4,5)
problems240_a(3,5)
problems240_a(1,10)

=======
Suggestion 9

def isConnect(a,b):
    if a == 1 and b == 3:
        return True
    if a == 1 and b == 4:
        return True
    if a == 1 and b == 5:
        return True
    if a == 1 and b == 6:
        return True
    if a == 2 and b == 3:
        return True
    if a == 2 and b == 4:
        return True
    if a == 2 and b == 5:
        return True
    if a == 2 and b == 6:
        return True
    if a == 3 and b == 5:
        return True
    if a == 3 and b == 6:
        return True
    if a == 4 and b == 5:
        return True
    if a == 4 and b == 6:
        return True
    if a == 5 and b == 6:
        return True
    return False

=======
Suggestion 10

def judge(a,b):
    if a==1 and b==2:
        print('Yes')
    elif a==1 and b==3:
        print('Yes')
    elif a==1 and b==4:
        print('Yes')
    elif a==1 and b==5:
        print('No')
    elif a==1 and b==6:
        print('No')
    elif a==1 and b==7:
        print('Yes')
    elif a==1 and b==8:
        print('No')
    elif a==1 and b==9:
        print('Yes')
    elif a==1 and b==10:
        print('Yes')
    elif a==2 and b==3:
        print('No')
    elif a==2 and b==4:
        print('No')
    elif a==2 and b==5:
        print('No')
    elif a==2 and b==6:
        print('No')
    elif a==2 and b==7:
        print('Yes')
    elif a==2 and b==8:
        print('No')
    elif a==2 and b==9:
        print('Yes')
    elif a==2 and b==10:
        print('Yes')
    elif a==3 and b==4:
        print('No')
    elif a==3 and b==5:
        print('No')
    elif a==3 and b==6:
        print('No')
    elif a==3 and b==7:
        print('Yes')
    elif a==3 and b==8:
        print('No')
    elif a==3 and b==9:
        print('Yes')
    elif a==3 and b==10:
        print('Yes')
    elif a==4 and b==5:
        print('Yes')
    elif a==4 and b==6:
        print('Yes')
    elif a==4 and b==7:
        print('Yes')
    elif a==4 and b==8:
        print('Yes')
    elif a==4 and b==9:
        print('Yes')
    elif a==4 and b==10:
        print('Yes')
    elif a==5 and b==6:
        print('Yes')
    elif a==5 and b==7:
        print('No')
    elif a==5 and b==8:
        print('No')
