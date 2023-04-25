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
        print('expert')

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
        print("expert")

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
    score = int(input())
    if score < 40:
        print(40 - score)
    elif score < 70:
        print(70 - score)
    elif score < 90:
        print(90 - score)
    else:
        print('expert')

=======
Suggestion 5

def main():
    x = int(input())
    if x >= 90:
        print("expert")
    elif x >= 70:
        print(90 - x)
    elif x >= 40:
        print(70 - x)
    else:
        print(40 - x)
    return 0

=======
Suggestion 6

def main():
    X = int(input())
    if X >= 0 and X < 40:
        print(40 - X)
    elif X >= 40 and X < 70:
        print(70 - X)
    elif X >= 70 and X < 90:
        print(90 - X)
    else:
        print("expert")
main()

=======
Suggestion 7

def main():
    x = int(input())
    if x == 0:
        print(40)
    elif x == 40:
        print(40)
    elif x == 80:
        print(20)
    elif x == 100:
        print("expert")
    else:
        print(40 - (x % 40))

=======
Suggestion 8

def main():
    # get the score
    score = int(input())
    # if the score is less than 40 print 40 - score
    if score < 40:
        print(40 - score)
    # if the score is less than 70 print 70 - score
    elif score < 70:
        print(70 - score)
    # if the score is less than 90 print 90 - score
    elif score < 90:
        print(90 - score)
    # if the score is less than 100 print expert
    elif score < 100:
        print("expert")
    # if the score is 100 print expert
    elif score == 100:
        print("expert")
