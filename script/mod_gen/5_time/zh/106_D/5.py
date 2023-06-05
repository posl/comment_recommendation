def findNumOfTrain(N,M,Q,train,query):
    #train = [[1, 1], [1, 2], [2, 2]]
    #query = [[1, 2]]
    result = []
    for i in range(Q):
        numOfTrain = 0
        for j in range(M):
            if train[j][0] >= query[i][0] and train[j][1] <= query[i][1]:
                numOfTrain += 1
        result.append(numOfTrain)
    return result

if __name__ == '__main__':
    findNumOfTrain()