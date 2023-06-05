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
