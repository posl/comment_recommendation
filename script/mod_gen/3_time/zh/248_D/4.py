def findNums(L,R,X):
    count = 0
    for i in range(L-1,R):
        if A[i] == X:
            count += 1
    return count

if __name__ == '__main__':
    findNums()