def isPass(score, k, n):
    if score[0] + score[1] + score[2] >= k:
        return True
    else:
        return False

if __name__ == '__main__':
    isPass()