def getStrList():
    N, K = map(int, input().split())
    strList = []
    for i in range(N):
        strList.append(input())
    return strList

if __name__ == '__main__':
    getStrList()