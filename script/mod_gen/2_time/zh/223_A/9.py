def judge(X):
    if X>=100 and X%100==0:
        return True
    else:
        return False
X = int(input())

if __name__ == '__main__':
    judge()