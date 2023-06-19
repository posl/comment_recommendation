def main():
    n = int(input())
    s = []
    t = []
    for i in range(n):
        x,y = map(int,input().split())
        s.append([x,y])
    for i in range(n):
        x,y = map(int,input().split())
        t.append([x,y])
    s.sort()
    t.sort()
    s_x = s[0][0]
    s_y = s[0][1]
    t_x = t[0][0]
    t_y = t[0][1]
    for i in range(n):
        s[i][0] -= s_x
        s[i][1] -= s_y
        t[i][0] -= t_x
        t[i][1] -= t_y
    s.sort(key = lambda x: (x[0],x[1]))
    t.sort(key = lambda x: (x[0],x[1]))
    if s == t:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()