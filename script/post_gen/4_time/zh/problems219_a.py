Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_next_level_score(score):
    if score >= 90:
        return "expert"
    elif score >= 70:
        return 90 - score
    elif score >= 40:
        return 70 - score
    else:
        return 40 - score

=======
Suggestion 2

def get_score():
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
        print('expert')

=======
Suggestion 4

def problems219_a():
    x = int(input())
    if x < 40:
        print(40-x)
    elif x < 70:
        print(70-x)
    elif x < 90:
        print(90-x)
    else:
        print("

=======
Suggestion 5

def main():
    x = int(input())
    if x >= 0 and x < 40:
        print(40 - x)
    elif x >= 40 and x < 70:
        print(70 - x)
    elif x >= 70 and x < 90:
        print(90 - x)

=======
Suggestion 6

def main():
    x = int(input())
    if x >= 90:
        print("expert")
    elif x >= 70:
        print(90-x)
    elif x >= 40:
        print(70-x)
    else:
        print(40-x)

=======
Suggestion 7

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
Suggestion 8

def main():
    X = int(input())
    if X >= 0 and X < 40:
        print(40 - X)
    elif X >= 40 and X < 70:
        print(70 - X)
    elif X >= 70 and X < 90:
        print(90 - X)

=======
Suggestion 9

def get_score(score):
    if score >= 90:
        return 'expert'
    elif score >= 70:
        return 90 - score
    elif score >= 40:
        return 70 - score
    else:
        return 40 - score
