Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    a = int(input())
    b = int(input())
    if a == 1:
        if b == 2:
            print(3)
        else:
            print(2)
    elif a == 2:
        if b == 1:
            print(3)
        else:
            print(1)
    else:
        if b == 1:
            print(2)
        else:
            print(1)

=======
Suggestion 2

def main():
    a = int(input())
    b = int(input())

    if a == 1 and b == 2:
        print(3)
    elif a == 1 and b == 3:
        print(2)
    elif a == 2 and b == 1:
        print(3)
    elif a == 2 and b == 3:
        print(1)
    elif a == 3 and b == 1:
        print(2)
    elif a == 3 and b == 2:
        print(1)

=======
Suggestion 3

def main():
    a = int(input())
    b = int(input())

    if a == 1 and b == 2:
        print(3)
    elif a == 2 and b == 1:
        print(3)
    elif a == 2 and b == 3:
        print(1)
    elif a == 3 and b == 2:
        print(1)
    elif a == 1 and b == 3:
        print(2)
    elif a == 3 and b == 1:
        print(2)

=======
Suggestion 4

def main():
    a = int(input())
    b = int(input())
    print(6 - a - b)

=======
Suggestion 5

def main():
    # a = int(input())
    # b = int(input())
    # print(6-a-b)
    print(6-int(input())-int(input()))

=======
Suggestion 6

def main():
  a = int(input())
  b = int(input())
  print(6-a-b)

main()
