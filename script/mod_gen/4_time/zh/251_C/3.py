def bestPoem():
    n=int(input())
    poem={}
    for i in range(n):
        s,t=input().split()
        if s in poem:
            if poem[s][0]<int(t):
                poem[s]=[int(t),i+1]
        else:
            poem[s]=[int(t),i+1]
    best=0
    bestPoem=''
    for i in poem:
        if poem[i][0]>best:
            best=poem[i][0]
            bestPoem=i
    return poem[bestPoem][1]

if __name__ == '__main__':
    bestPoem()