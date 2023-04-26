Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a, b = map(int, input().split())
    if a == 1 and b == 10:
        print("Yes")
    elif a == 10 and b == 1:
        print("Yes")
    elif abs(a-b) == 1:
        print("Yes")
    else:
        print("No")

=======
Suggestion 2

def main():
    a, b = map(int, input().split())
    if a == 1 and b == 3:
        print("Yes")
    elif a == 1 and b == 5:
        print("Yes")
    elif a == 1 and b == 7:
        print("Yes")
    elif a == 1 and b == 9:
        print("Yes")
    elif a == 2 and b == 3:
        print("Yes")
    elif a == 2 and b == 6:
        print("Yes")
    elif a == 2 and b == 8:
        print("Yes")
    elif a == 2 and b == 10:
        print("Yes")
    elif a == 3 and b == 4:
        print("Yes")
    elif a == 3 and b == 5:
        print("Yes")
    elif a == 3 and b == 9:
        print("Yes")
    elif a == 3 and b == 10:
        print("Yes")
    elif a == 4 and b == 7:
        print("Yes")
    elif a == 4 and b == 8:
        print("Yes")
    elif a == 4 and b == 9:
        print("Yes")
    elif a == 4 and b == 10:
        print("Yes")
    elif a == 5 and b == 6:
        print("Yes")
    elif a == 5 and b == 7:
        print("Yes")
    elif a == 5 and b == 8:
        print("Yes")
    elif a == 5 and b == 9:
        print("Yes")
    elif a == 6 and b == 7:
        print("Yes")
    elif a == 6 and b == 8:
        print("Yes")
    elif a == 6 and b == 10:
        print("Yes")
    elif a == 7 and b == 8:
        print("Yes")
    elif a == 7 and b == 9:
        print("Yes")
    elif a == 7 and b == 10:
        print("Yes")
    elif a == 8 and b == 9:
        print("Yes")
    elif a == 8 and b == 10:
        print("Yes")
    elif a == 9 and b ==

=======
Suggestion 3

def main():
    a, b = map(int, input().split())
    if a == 1:
        if b == 2 or b == 3:
            print("Yes")
        else:
            print("No")
    elif a == 2:
        if b == 4 or b == 5:
            print("Yes")
        else:
            print("No")
    elif a == 3:
        if b == 6 or b == 7:
            print("Yes")
        else:
            print("No")
    elif a == 4:
        if b == 8 or b == 9:
            print("Yes")
        else:
            print("No")
    elif a == 5:
        if b == 10:
            print("Yes")
        else:
            print("No")
    elif a == 6:
        if b == 8 or b == 10:
            print("Yes")
        else:
            print("No")
    elif a == 7:
        if b == 9 or b == 10:
            print("Yes")
        else:
            print("No")
    elif a == 8:
        if b == 10:
            print("Yes")
        else:
            print("No")
    elif a == 9:
        if b == 10:
            print("Yes")
        else:
            print("No")
    elif a == 10:
        print("Yes")

main()

=======
Suggestion 4

def main():
    a, b = map(int, input().split())
    if a + 1 == b or a - 1 == b or a == 10 and b == 1 or a == 1 and b == 10:
        print("Yes")
    else:
        print("No")

=======
Suggestion 5

def main():
    a, b = map(int, input().split())
    if a == 1 and b == 10:
        print("Yes")
    elif a <= 4 and b <= 4:
        print("Yes")
    elif a >= 7 and b >= 7:
        print("Yes")
    else:
        print("No")

=======
Suggestion 6

def main():
    a, b = map(int, input().split())
    if a + 1 == b or a - 1 == b or a + 8 == b or a - 8 == b:
        print("Yes")
    else:
        print("No")

=======
Suggestion 7

def main():
    a, b = map(int, input().split())
    if a == 1 and b == 10:
        print("Yes")
    elif a <= 4 and b <= 4:
        print("Yes")
    else:
        print("No")

=======
Suggestion 8

def main():
    a, b = map(int, input().split())
    if a <= 3 <= b or a <= 7 <= b:
        print('Yes')
    else:
        print('No')

=======
Suggestion 9

def main():
    a,b = map(int,input().split())
    if a <= b:
        if a <= 4 and b >= 5:
            print("Yes")
        else:
            print("No")
    else:
        if b <= 4 and a >= 5:
            print("Yes")
        else:
            print("No")
