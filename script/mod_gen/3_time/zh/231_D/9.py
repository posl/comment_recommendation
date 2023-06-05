def findfather(x):
    if x != father[x]:
        father[x] = findfather(father[x])
    return father[x]

if __name__ == '__main__':
    findfather()