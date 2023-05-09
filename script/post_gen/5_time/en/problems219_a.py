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
Suggestion 3

def main():
    points = int(input())
    if points < 40:
        print(40 - points)
    elif points < 70:
        print(70 - points)
    elif points < 90:
        print(90 - points)
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
        print("expert")

=======
Suggestion 5

def main():
    score = int(input())
    if 0 <= score < 40:
        print(40 - score)
    elif 40 <= score < 70:
        print(70 - score)
    elif 70 <= score < 90:
        print(90 - score)
    else:
        print('expert')

=======
Suggestion 6

def rank(x):
    if x >= 0 and x < 40:
        return 40 - x
    elif x >= 40 and x < 70:
        return 70 - x
    elif x >= 70 and x < 90:
        return 90 - x
    elif x >= 90 and x <= 100:
        return "expert"
    else:
        return -1

x = int(input())
print(rank(x))

=======
Suggestion 7

def get_extra_points(x):
    if x <= 39:
        return 40 - x
    elif x <= 69:
        return 70 - x
    elif x <= 89:
        return 90 - x
    return "expert"
