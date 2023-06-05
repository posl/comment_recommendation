def dist(x1,y1,x2,y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
n=int(input())
towns=[]
for i in range(n):
    towns.append(list(map(int,input().split())))

if __name__ == '__main__':
    dist()