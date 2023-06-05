def problems108_b():
    x1,y1,x2,y2 = map(int,input().split())
    x3,y3 = x2-y2+y1,x2-x1+y2
    x4,y4 = x1-y2+y1,x2-x1+y1
    print(x3,y3,x4,y4)

if __name__ == '__main__':
    problems108_b()