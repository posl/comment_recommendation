def main():
    n,m,x = map(int,input().split())
    #n,m,x = 3,3,10
    #n,m,x = 3,3,10
    #n,m,x = 8,5,22
    #c = [60,70,50]
    #a = [[2,2,4],[8,7,9],[2,3,9]]
    #c = [100,100,100]
    #a = [[3,1,4],[1,5,9],[2,6,5]]
    #c = [100,164,334,234,541,235,394,872]
    #a = [[3,7,5,3,1],[4,5,2,7,8],[7,2,7,2,9],[4,7,2,8,2],[5,4,3,3,6],[4,8,6,9,7],[3,6,1,6,2],[8,4,3,7,2]]
    c = []
    a = []
    for i in range(n):
        c.append(list(map(int,input().split())))
        #c.append(list(map(int,input().split())))
        a.append(c[i][1:])
        c[i] = c[i][0]
    #print(c)
    #print(a)
    #print(n,m,x)
    #print(c)
    #print(a)
    #print(c)
    #print(a)
    #print(n,m,x)
    #print(c)
