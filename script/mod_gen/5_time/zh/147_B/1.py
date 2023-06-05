def judge(s):
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True

if __name__ == '__main__':
    judge()