Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def get_score(score):
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
        print('expert')

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

def get_score_rank(score):
    if score >= 0 and score < 40:
        return "新手"
    elif score >= 40 and score < 70:
        return "中级"
    elif score >= 70 and score < 90:
        return "高级"
    elif score >= 90 and score <= 100:
        return "专家"
    else:
        return "输入错误"

=======
Suggestion 6

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
Suggestion 7

def main():
    x = int(input())
    if x >= 0 and x < 40:
        print(40-x)
    elif x >= 40 and x < 70:
        print(70-x)
    elif x >= 70 and x < 90:
        print(90-x)
    else:
        print("专家")

=======
Suggestion 8

def get_level(score):
    if score < 40:
        return '新手'
    elif score < 70:
        return '中级'
    elif score < 90:
        return '高级'
    else:
        return '专家'

=======
Suggestion 9

def get_score_level(score):
    if score < 40:
        return "新手"
    elif score < 70:
        return "中级"
    elif score < 90:
        return "高级"
    else:
        return "专家"
