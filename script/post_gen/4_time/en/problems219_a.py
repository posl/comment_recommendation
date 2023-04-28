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
    score = int(input())
    if score < 40:
        print(40 - score)
    elif score < 70:
        print(70 - score)
    elif score < 90:
        print(90 - score)
    else:
        print("expert")

=======
Suggestion 3

def main():
    x = int(input())
    if x >= 0 and x < 40:
        print(40 - x)
    elif x >= 40 and x < 70:
        print(70 - x)
    elif x >= 70 and x < 90:
        print(90 - x)
    else:
        print("expert")

=======
Suggestion 4

def rank(x):
    if x >= 0 and x < 40:
        return 40 - x
    elif x >= 40 and x < 70:
        return 70 - x
    elif x >= 70 and x < 90:
        return 90 - x
    else:
        return "expert"

=======
Suggestion 5

def main():
    x = int(input())
    if x >= 90:
        print('expert')
    elif x >= 70:
        print(90-x)
    elif x >= 40:
        print(70-x)
    else:
        print(40-x)

=======
Suggestion 6

def getRank(score):
    if score >= 0 and score < 40:
        return "D"
    elif score >= 40 and score < 70:
        return "C"
    elif score >= 70 and score < 90:
        return "B"
    elif score >= 90:
        return "A"
    else:
        return "Error"

=======
Suggestion 7

def problems219_a():
    score = int(input())

    if score < 40:
        print(40 - score)
    elif score < 70:
        print(70 - score)
    elif score < 90:
        print(90 - score)
    else:
        print("expert")

=======
Suggestion 8

def main():
    # Take input from user
    x = int(input())

    if x >= 0 and x < 40:
        print(40 - x)
    elif x >= 40 and x < 70:
        print(70 - x)
    elif x >= 70 and x < 90:
        print(90 - x)
    else:
        print('expert')
