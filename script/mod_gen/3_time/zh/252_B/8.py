def judge_like(food,unlike):
    for i in range(len(unlike)):
        if food == unlike[i]:
            return True
    return False

if __name__ == '__main__':
    judge_like()