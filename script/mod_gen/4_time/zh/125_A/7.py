def calNum(A,B,T):
    num = 0
    for i in range(1,T+1):
        if i%A == 0:
            num += B
    return num

if __name__ == '__main__':
    calNum()