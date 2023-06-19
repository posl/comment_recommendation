def judge_pair(a):
    if len(a) == len(set(a)):
        return True
    else:
        return False

if __name__ == '__main__':
    judge_pair()