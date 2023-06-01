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

def get_score_level(score):
    if score >= 0 and score < 40:
        return "新手"
    elif score >= 40 and score < 70:
        return "中级"
    elif score >= 70 and score < 90:
        return "高级"
    elif score >= 90 and score <= 100:
        return "专家"
    else:
        return "输入分数有误"

=======
Suggestion 3

def main():
    x = int(input())
    if x < 40:
        print(40-x)
    elif x < 70:
        print(70-x)
    elif x < 90:
        print(90-x)
    else:
        print('专家')

=======
Suggestion 4

def get_level(score):
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
Suggestion 5

def get_level(x):
    if x < 40:
        return 40
    elif x < 70:
        return 70
    elif x < 90:
        return 90
    else:
        return 'expert'

=======
Suggestion 6

def getScore():
    score = int(input())
    if score >= 0 and score < 40:
        print(40-score)
    elif score >= 40 and score < 70:
        print(70-score)
    elif score >= 70 and score < 90:
        print(90-score)
    elif score >= 90 and score <= 100:
        print('专家')
    else:
        print('输入错误')

getScore()

=======
Suggestion 7

def exam_grade(n):
    if n < 40:
        return 40 - n
    elif n < 70:
        return 70 - n
    elif n < 90:
        return 90 - n
    else:
        return 'expert'

n = int(input())
print(exam_grade(n))

=======
Suggestion 8

def get_score():
    while True:
        score = input("请输入你的分数：")
        if score.isdigit():
            score = int(score)
            if score >= 0 and score <= 100:
                break
            else:
                print("请输入0到100之间的数字")
                continue
        else:
            print("请输入数字")
            continue
    return score

=======
Suggestion 9

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
