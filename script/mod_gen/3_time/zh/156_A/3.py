def judge(N,R):
    if N>=10:
        return R
    else:
        return R+(10-N)*100

if __name__ == '__main__':
    judge()