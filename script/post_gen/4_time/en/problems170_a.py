Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    # input
    x_1, x_2, x_3, x_4, x_5 = map(int, input().split())

    # compute

    # output
    if x_1 == 0:
        print(1)
    elif x_2 == 0:
        print(2)
    elif x_3 == 0:
        print(3)
    elif x_4 == 0:
        print(4)
    else:
        print(5)

=======
Suggestion 2

def main():
    x = list(map(int, input().split()))
    for i in range(len(x)):
        if x[i] == 0:
            print(i+1)

=======
Suggestion 3

def main():
    x = list(map(int, input().split()))

    for i in range(5):
        if x[i] == 0:
            print(i + 1)
            break

=======
Suggestion 4

def main():
    x = input().split()
    for i in range(5):
        if x[i] == '0':
            print(i+1)
            break

=======
Suggestion 5

def main():
    x = input().split()
    for i in range(0, len(x)):
        if x[i] == '0':
            print(i+1)

=======
Suggestion 6

def main():
    x = list(map(int, input().split()))
    print(x.index(0)+1)

=======
Suggestion 7

def main():
    x = input().split()
    for i in range(5):
        if int(x[i]) == 0:
            print(i+1)
            break

main()

=======
Suggestion 8

def main():
    x = input()
    print(x.split().index('0')+1)

=======
Suggestion 9

def main():
    import sys

    #input
    x = list(map(int, sys.stdin.readline().strip().split()))
    print(x.index(0)+1)
