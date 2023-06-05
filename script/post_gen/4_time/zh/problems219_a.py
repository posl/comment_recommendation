Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def test():
    x = int(input())
    if x >= 90:
        print('专家')
    elif x >= 70:
        print(90 - x)
    elif x >= 40:
        print(70 - x)
    else:
        print(40 - x)
test()

=======
Suggestion 2

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
Suggestion 3

def get_grade(score):
    if score >= 90:
        return 'expert'
    elif score >= 70:
        return 'high'
    elif score >= 40:
        return 'middle'
    else:
        return 'newbie'

=======
Suggestion 4

def main():
    x = int(input())
    if x < 40:
        print(40-x)
    elif x < 70:
        print(70-x)
    elif x < 90:
        print(90-x)
    else:
        print("专家")

=======
Suggestion 5

def level(x):
    if x >= 0 and x < 40:
        return 1
    elif x >= 40 and x < 70:
        return 2
    elif x >= 70 and x < 90:
        return 3
    else:
        return 4

=======
Suggestion 6

def main():
    X = int(input())
    if X < 40:
        print(40 - X)
    elif X < 70:
        print(70 - X)
    elif X < 90:
        print(90 - X)
    else:
        print("专家")

=======
Suggestion 7

def problem219_a():
    x = int(input())
    if x < 40:
        print(40 - x)
    elif x < 70:
        print(70 - x)
    elif x < 90:
        print(90 - x)
    else:
        print('专家')

=======
Suggestion 8

def getLevel(score):
    if score >= 0 and score < 40:
        return '新手'
    elif score >= 40 and score < 70:
        return '中级'
    elif score >= 70 and score < 90:
        return '高级'
    elif score >= 90 and score <= 100:
        return '专家'
    else:
        return '输入错误'

=======
Suggestion 9

def calc_score(score):
    if score >= 0 and score < 40:
        return 40 - score
    elif score >= 40 and score < 70:
        return 70 - score
    elif score >= 70 and score < 90:
        return 90 - score
    else:
        return "expert"
