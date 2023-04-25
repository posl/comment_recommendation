Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    y = int(input())
    while True:
        if y % 4 == 2:
            print(y)
            break
        y += 1

=======
Suggestion 2

def main():
    year = int(input())
    while True:
        if year % 4 == 2:
            print(year)
            break
        else:
            year += 1

=======
Suggestion 3

def main():
    Y = int(input())
    for i in range(Y, 3000):
        if i % 4 == 2:
            print(i)
            break

=======
Suggestion 4

def main():
    y = int(input())
    if y%4 == 2:
        print(y)
    else:
        print(y + 4 - y%4)

=======
Suggestion 5

def main():
    #input
    y = int(input())
    #calculate
    while True:
        if y % 4 == 2:
            break
        else:
            y += 1
    #output
    print(y)

main()

=======
Suggestion 6

def main():
    y = int(input())
    y += 4 - y % 4
    print(y)

=======
Suggestion 7

def main():
    y = int(input())
    print(y + (4 - y % 4))

=======
Suggestion 8

def main():
    # Get input
    Y = int(input())

    # Find next event
    if Y % 4 == 2:
        print(Y)
    else:
        print(Y + 2 - (Y % 4))

=======
Suggestion 9

def main():
    # get input
    y = int(input())

    # solve
    ans = y + 2 - (y % 4)

    # output
    print(ans)
