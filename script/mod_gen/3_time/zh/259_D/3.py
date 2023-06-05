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
