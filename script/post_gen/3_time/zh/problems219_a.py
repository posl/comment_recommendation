Synthesizing 10/10 solutions

=======
Suggestion 1

def get_level(score):
    if score >= 90:
        return "expert"
    elif score >= 70:
        return "high"
    elif score >= 40:
        return "intermediate"
    else:
        return "beginner"

=======
Suggestion 2

def get_rank(score):
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
Suggestion 3

def get_level(score):
    if score >= 90:
        return "expert"
    elif score >= 70:
        return "high"
    elif score >= 40:
        return "middle"
    else:
        return "beginner"

=======
Suggestion 4

def main():
    x = int(input())
    if x >= 0 and x < 40:
        print(40 - x)
    elif x >= 40 and x < 70:
        print(70 - x)
    elif x >= 70 and x < 90:
        print(90 - x)
    elif x >= 90 and x <= 100:
        print("专家")

=======
Suggestion 5

def main():
    score = int(input())
    if score >= 90:
        print('expert')
    elif score >= 70:
        print(90 - score)
    elif score >= 40:
        print(70 - score)
    else:
        print(40 - score)

=======
Suggestion 6

def main():
    x = input()
    x = int(x)
    if 0 <= x < 40:
        print(40 - x)
    elif 40 <= x < 70:
        print(70 - x)
    elif 70 <= x < 90:
        print(90 - x)
    else:
        print("专家")

=======
Suggestion 7

def getGrade(n):
    if n >= 0 and n < 40:
        return 40 - n
    elif n >= 40 and n < 70:
        return 70 - n
    elif n >= 70 and n < 90:
        return 90 - n
    else:
        return "expert"

=======
Suggestion 8

def main():
    x = int(input())
    if 0 <= x < 40:
        print(40 - x)
    elif 40 <= x < 70:
        print(70 - x)
    elif 70 <= x < 90:
        print(90 - x)
    else:
        print("专家")

=======
Suggestion 9

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
Suggestion 10

def test_219_a():
    input = 56
    output = 14
    assert output == solve(input)

    input = 32
    output = 8
    assert output == solve(input)

    input = 0
    output = 40
    assert output == solve(input)

    input = 100
    output = '专家'
    assert output == solve(input)
