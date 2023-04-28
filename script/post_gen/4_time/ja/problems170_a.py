Synthesizing 10/10 solutions

=======
Suggestion 1

def main():
    # input
    x1, x2, x3, x4, x5 = map(int, input().split())

    # compute

    # output
    if x1 == 0:
        print(1)
    elif x2 == 0:
        print(2)
    elif x3 == 0:
        print(3)
    elif x4 == 0:
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
            break

=======
Suggestion 3

def main():
    x = list(map(int, input().split()))
    for i in range(len(x)):
        if x[i] == 0:
            print(i+1)
            return

=======
Suggestion 4

def main():
    x = list(map(int, input().split()))
    for i in range(5):
        if x[i] == 0:
            print(i+1)

=======
Suggestion 5

def main():
    x_1, x_2, x_3, x_4, x_5 = map(int, input().split())
    for i in range(1, 6):
        if eval("x_" + str(i)) == 0:
            print(i)
            break

=======
Suggestion 6

def main():
    x_list = list(map(int, input().split()))
    for i in range(5):
        if x_list[i] == 0:
            print(i+1)
            break

=======
Suggestion 7

def main():
    x = input().split()
    for i in range(5):
        if x[i] == '0':
            print(i+1)
            break

=======
Suggestion 8

def main():
    x = input().rstrip().split()
    for i in range(len(x)):
        if x[i] == '0':
            print(i+1)
            break

=======
Suggestion 9

def main():
    x = list(map(int, input().split()))
    print(x.index(0)+1)

=======
Suggestion 10

def main():
    x = list(map(int, input().strip().split()))
    print(x.index(0)+1)
