def judge_easy(s):
    if len(s) == 1:
        return True
    #奇数位置
    for i in range(0, len(s), 2):
        if s[i] in ['L', 'D']:
            return False
    #偶数位置
    for i in range(1, len(s), 2):
        if s[i] in ['R', 'D']:
            return False
    return True

if __name__ == '__main__':
    judge_easy()