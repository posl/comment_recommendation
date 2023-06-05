Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def main():
    pass

=======
Suggestion 2

def main():
    print("Hello World!")

=======
Suggestion 3

def solve():
    pass

=======
Suggestion 4

def main():
    n=int(input())
    s_x,s_y,t_x,t_y=map(int,input().split())
    xy=[]
    for i in range(n):
        xy.append(list(map(int,input().split())))
    #print(xy)
    for i in range(n):
        if (xy[i][0]-s_x)**2+(xy[i][1]-s_y)**2<xy[i][2]**2 and (xy[i][0]-t_x)**2+(xy[i][1]-t_y)**2<xy[i][2]**2:
            print("No")
            exit()
    print("Yes")
main()

=======
Suggestion 5

def main():
    N = int(input())
    S_X, S_Y, T_X, T_Y = map(int, input().split())
    circles = []
    for _ in range(N):
        circles.append(list(map(int, input().split())))

    def check(x, y):
        for i in range(N):
            if (x - circles[i][0]) ** 2 + (y - circles[i][1]) ** 2 > circles[i][2] ** 2:
                return False
        return True

    def solve():
        for i in range(N):
            if check(circles[i][0], circles[i][1]):
                return True
        return False

    if solve():
        print('Yes')
    else:
        print('No')
