Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    y = int(input())
    if y % 4 == 2:
        print(y)
    else:
        print(y + (4 - (y % 4)))

=======
Suggestion 2

def main():
    Y = int(input())
    while True:
        if Y % 4 == 2:
            print(Y)
            break
        Y += 1

=======
Suggestion 3

def main():
    y = int(input())
    if y % 4 == 2:
        print(y)
    else:
        print(y + 4 - (y % 4))

=======
Suggestion 4

def main():
    Y = int(input())
    if Y % 4 == 2:
        print(Y)
    else:
        print(Y + 2 - Y % 4)

=======
Suggestion 5

def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            break
        else:
            y += 1
    return

=======
Suggestion 6

def main():
    y = int(input())
    while(True):
        if y % 4 == 2:
            print(y)
            break
        else:
            y += 1

main()

=======
Suggestion 7

def main():
    Y = int(input())
    #Y = 2022
    #Y = 2023
    #Y = 3000
    
    if Y % 4 == 2:
        print(Y)
    else:
        print(Y + (4 - Y % 4))

=======
Suggestion 8

def main():
    y = int(input())
    for i in range(4):
        if (y+i)%4 == 2:
            print(y+i)
            break

=======
Suggestion 9

def main():
    Y = int(input())
    while Y%4 != 2:
        Y += 1
    print(Y)

=======
Suggestion 10

def main():
    # Y: 2000 ≦ Y ≦ 3000
    Y = int(input())
    if Y % 4 == 2:
        print(Y)
    else:
        print(Y + 4 - Y % 4)
