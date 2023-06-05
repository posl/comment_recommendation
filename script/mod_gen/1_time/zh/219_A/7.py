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

if __name__ == '__main__':
    get_score()