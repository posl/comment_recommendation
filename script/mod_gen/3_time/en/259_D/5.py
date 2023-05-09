def main():
    #input
    N = int(input())
    s_x,s_y,t_x,t_y = map(int,input().split())
    circles = []
    for i in range(N):
        x,y,r = map(int,input().split())
        circles.append([x,y,r])
    #solve
    def dist(x1,y1,x2,y2):
        return ((x1-x2)**2+(y1-y2)**2)**0.5
    def dist2(x1,y1,x2,y2):
        return (x1-x2)**2+(y1-y2)**2
    def is_in(x1,y1,x2,y2,r):
        return dist2(x1,y1,x2,y2) < r**2
    def is_on(x1,y1,x2,y2,r):
        return dist2(x1,y1,x2,y2) == r**2
    def is_cross(x1,y1,x2,y2,r):
        return dist2(x1,y1,x2,y2) < r**2 and dist2(x1,y1,x2,y2) > 0
    def is_cross2(x1,y1,x2,y2,r):
        return dist2(x1,y1,x2,y2) < r**2 and dist2(x1,y1,x2,y2) == 0
    def is_cross3(x1,y1,x2,y2,r):
        return dist2(x1,y1,x2,y2) == r**2 and dist2(x1,y1,x2,y2) > 0
    def is_cross4(x1,y1,x2,y2,r):
        return dist2(x1,y1,x2,y2) > r**2 and dist2(x1,y1,x2,y2) > 0
    def is_cross_circle(x1,y1,x2,y2,x3,y3,r):
        if is_in(x1,y1,x3,y3,r):
            return True
        elif is_in(x2,y2,x3,y3,r):
            return True
        elif is_on(x1,y1,x3,y3,r):
            return True
        elif is_on(x2,y2,x3,y3,r):
            return True
        elif is_cross(x1,y1,x2,y2,r):
            if is_cross4(x1,y1,x3,y3,r)

if __name__ == '__main__':
    main()