Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_grade(score):
    if score >= 0 and score < 40:
        return 'D'
    elif score >= 40 and score < 70:
        return 'C'
    elif score >= 70 and score < 90:

=======
Suggestion 2

def get_level(score):
    if score < 40:
        return 'D'
    elif score < 70:
        return 'C'
    elif score < 90:
        return 'B'
    else:
        return 'A'

=======
Suggestion 3

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
Suggestion 4

def get_score(score):
    if score >= 0 and score < 40:
        return 40 - score
    elif score >= 40 and score < 70:
        return 70 - score
    elif score >= 70 and

=======
Suggestion 5

def get_next_level_score(score):
    if score < 40:
        return 40 - score
    elif score < 70:
        return 70 - score
    elif score < 90:
        return 90 - score

=======
Suggestion 6

def main():
    score = int(input())
    if score >= 0 and score < 40:
        print(40 - score)
    elif score >= 40 and score < 70:
        print(70 - score)
    elif

=======
Suggestion 7

def get_next_grade_score(score):
    if score < 40:
        return 40 - score
    elif score < 70:
        return 70 - score
    elif score < 90:
        return 90 - score

=======
Suggestion 8

def get_score(grade):
    if grade == 'D':
        return 0
    elif grade == 'C':
        return 1
    elif grade == 'B':
        return 2
    elif grade == 'A':

=======
Suggestion 9

def solve():
    X = int(input())
    if X < 40:
        print(40 - X)
    elif X < 70:
        print(70 - X)
    elif X < 90:
        print(90 - X)
    else:
        print('expert')
