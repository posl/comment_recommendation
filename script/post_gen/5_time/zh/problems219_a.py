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
        print("专家")

=======
Suggestion 2

def get_score_level(score):
    if score >= 0 and score < 40:
        return "新手"
    elif score >= 40 and score < 70:
        return "中级"
    elif score >= 70 and score < 90:
        return "高级"
    else:
        return "专家"

=======
Suggestion 3

def print_level(X):
    if X >= 0 and X < 40:
        print(40 - X)
    elif X >= 40 and X < 70:
        print(70 - X)
    elif X >= 70 and X < 90:
        print(90 - X)
    else:
        print('expert')

=======
Suggestion 4

def get_score(score):
    if score < 40:
        return 40 - score
    elif score < 70:
        return 70 - score
    elif score < 90:
        return 90 - score
    else:
        return 'expert'

=======
Suggestion 5

def main():
    score = int(input())
    if score < 40:
        print(40 - score)
    elif score < 70:
        print(70 - score)
    elif score < 90:
        print(90 - score)
    else:
        print("专家")

=======
Suggestion 6

def problem219_a():
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
Suggestion 7

def get_grade(x):
    if 0 <= x < 40:
        return 40 - x
    elif 40 <= x < 70:
        return 70 - x
    elif 70 <= x < 90:
        return 90 - x
    else:
        return '专家'
