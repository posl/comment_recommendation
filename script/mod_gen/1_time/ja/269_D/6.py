def main():
    n = int(input())
    x = []
    y = []
    for i in range(n):
        a,b = map(int,input().split())
        x.append(a)
        y.append(b)
    #print(x)
    #print(y)
    p = []
    for i in range(n):
        p.append([x[i],y[i]])
    #print(p)
    #print(p[0][0])
    #print(p[0][1])
    #print(p[0][0]+p[0][1])
    #print(p[0][0]-p[0][1])
    #print(p[0][0]+p[0][1]+p[0][0]-p[0][1])
    #print(p[0][0]+p[0][1]-p[0][0]+p[0][1])
    #print(p[0][0]+p[0][1]+p[0][0]-p[0][1]+p[0][0]+p[0][1]-p[0][0]+p[0][1])
    #print(p[0][0]+p[0][1]+p[0][0]-p[0][1]-p[0][0]-p[0][1])
    #print(p[0][0]+p[0][1]+p[0][0]-p[0][1]+p[0][0]+p[0][1]-p[0][0]+p[0][1]-p[0][0]-p[0][1])
    #print(p[0][0]+p[0][1]+p[0][0]-p[0][1]-p[0][0]-p[0][1]+p[0][0]+p[0][1])
    #print(p[0][0]+p[0][1]+p[0][0]-p[0][1]-p[0][0]-p[0][1]+p[0][0]+p[0][1]-p[0][0]-p[0][1])
    #print(p[0][0]+p[0][1]+p[0][0]-p[0][1]-p[0][0]-p[0][1]+p[0][0]+p[0][1]-p

if __name__ == '__main__':
    main()