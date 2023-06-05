def getMinOperateNum(A,X):
    # 计算A中每个元素到X的距离，然后求和
    sum = 0
    for i in range(len(A)):
        sum += abs(A[i] - X)
    return sum

if __name__ == '__main__':
    getMinOperateNum()