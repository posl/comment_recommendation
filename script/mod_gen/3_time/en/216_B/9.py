def readinput():
    n = int(input())
    stlist = []
    for _ in range(n):
        stlist.append(list(input().split()))
    return n,stlist

if __name__ == '__main__':
    readinput()