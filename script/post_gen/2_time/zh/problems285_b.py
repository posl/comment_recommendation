Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    a,b = map(int,input().split())
    if a+1 == b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a,b = map(int, input().split())
    if a == 1 and b == 2:
        print('Yes')
    elif a == 2 and b == 3:
        print('Yes')
    elif a == 3 and b == 4:
        print('Yes')
    elif a == 4 and b == 5:
        print('Yes')
    elif a == 5 and b == 6:
        print('Yes')
    elif a == 6 and b == 7:
        print('Yes')
    elif a == 7 and b == 8:
        print('Yes')
    elif a == 8 and b == 9:
        print('Yes')
    elif a == 9 and b == 10:
        print('Yes')
    elif a == 10 and b == 11:
        print('Yes')
    elif a == 11 and b == 12:
        print('Yes')
    elif a == 12 and b == 13:
        print('Yes')
    elif a == 13 and b == 14:
        print('Yes')
    elif a == 14 and b == 15:
        print('Yes')
    else:
        print('No')

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a in [1, 3, 5, 7, 9, 11, 13, 15] and b in [2, 4, 6, 8, 10, 12, 14]:
        print('Yes')
    else:
        print('No')

=======
Suggestion 4

def main():
    a,b = map(int, input().split())
    if (b-a) == 1 or (b-a) == 4 or (b-a) == 3:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a,b = map(int,input().split())
    if (a==1 and b==2) or (a==1 and b==3) or (a==2 and b==3) or (a==2 and b==4) or (a==3 and b==4) or (a==3 and b==5) or (a==4 and b==5) or (a==4 and b==6) or (a==5 and b==6) or (a==5 and b==7) or (a==6 and b==7) or (a==6 and b==8) or (a==7 and b==8) or (a==7 and b==9) or (a==8 and b==9) or (a==8 and b==10) or (a==9 and b==10) or (a==9 and b==11) or (a==10 and b==11) or (a==10 and b==12) or (a==11 and b==12) or (a==11 and b==13) or (a==12 and b==13) or (a==12 and b==14) or (a==13 and b==14) or (a==13 and b==15):
        print("Yes")
    else:
        print("No")
main()

=======
Suggestion 6

def main():
    a,b = map(int,input().split())
    if (a,b) in [(1,2),(1,3),(1,4),(3,4),(2,3),(2,4),(3,5),(4,5),(3,6),(4,6),(5,6),(5,7),(5,8),(6,8),(7,8),(6,9),(7,9),(8,9),(8,10),(9,10),(8,11),(9,11),(10,11),(10,12),(10,13),(11,13),(11,14),(12,13),(13,14),(13,15)]:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    a,b = map(int, input().split())
    if a == 8 or a == 9:
        if b == 8 or b == 9:
            print("Yes")
            return
    if a == 3 or a == 4:
        if b == 3 or b == 4:
            print("Yes")
            return
    if a == 6 or a == 7:
        if b == 6 or b == 7:
            print("Yes")
            return
    if a == 10 or a == 11:
        if b == 10 or b == 11:
            print("Yes")
            return
    print("No")

=======
Suggestion 8

def main():
    a,b = map(int,input().split())
    if a < b:
        if b - a == 1 or b - a == 4 or b - a == 3:
            print("Yes")
        else:
            print("No")
    else:
        if a - b == 1 or a - b == 4 or a - b == 3:
            print("Yes")
        else:
            print("No")

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    if b-a == 1 or b-a == 4 or b-a == 3:
        print("Yes")
    else:
        print("No")

=======
Suggestion 10

def is_connect(a, b):
    if (a == 1 and b == 2) or (b == 1 and a == 2):
        return True
    elif (a == 2 and b == 3) or (b == 2 and a == 3):
        return True
    elif (a == 3 and b == 4) or (b == 3 and a == 4):
        return True
    elif (a == 4 and b == 5) or (b == 4 and a == 5):
        return True
    elif (a == 5 and b == 6) or (b == 5 and a == 6):
        return True
    elif (a == 6 and b == 7) or (b == 6 and a == 7):
        return True
    elif (a == 7 and b == 8) or (b == 7 and a == 8):
        return True
    elif (a == 8 and b == 9) or (b == 8 and a == 9):
        return True
    elif (a == 9 and b == 10) or (b == 9 and a == 10):
        return True
    elif (a == 10 and b == 11) or (b == 10 and a == 11):
        return True
    elif (a == 11 and b == 12) or (b == 11 and a == 12):
        return True
    elif (a == 12 and b == 13) or (b == 12 and a == 13):
        return True
    elif (a == 13 and b == 14) or (b == 13 and a == 14):
        return True
    elif (a == 14 and b == 15) or (b == 14 and a == 15):
        return True
    else:
        return False
a, b = map(int, input().split())
