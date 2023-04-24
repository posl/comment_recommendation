Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    x = int(input())
    if x < 40:
        print(40 - x)
    elif x < 70:
        print(70 - x)
    elif x < 90:
        print(90 - x)
    else:
        print("expert")

=======
Suggestion 2

def main():
    x = int(input())
    if x < 40:
        print(40 - x)
    elif x < 70:
        print(70 - x)
    elif x < 90:
        print(90 - x)
    else:
        print('expert')

=======
Suggestion 3

def main():
    X = int(input())
    if X < 40:
        print(40 - X)
    elif X < 70:
        print(70 - X)
    elif X < 90:
        print(90 - X)
    else:
        print("expert")

=======
Suggestion 4

def main():
    X = int(input())
    if 0 <= X < 40:
        print(40 - X)
    elif 40 <= X < 70:
        print(70 - X)
    elif 70 <= X < 90:
        print(90 - X)
    elif 90 <= X <= 100:
        print("expert")

=======
Suggestion 5

def main():
    # input
    x = int(input())

    # compute
    if x < 40:
        ans = 40 - x
    elif x < 70:
        ans = 70 - x
    elif x < 90:
        ans = 90 - x
    else:
        ans = 'expert'

    # output
    print(ans)

=======
Suggestion 6

def main():
    # X = 56
    # X = 32
    # X = 0
    X = 100

    if X >= 0 and X < 40:
        print(40 - X)
    elif X >= 40 and X < 70:
        print(70 - X)
    elif X >= 70 and X < 90:
        print(90 - X)
    elif X >= 90 and X <= 100:
        print('expert')
    else:
        print('Error')
