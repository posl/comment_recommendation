def ball():
    s_x,s_y,g_x,g_y = map(int,input().split())
    #print(s_x,s_y,g_x,g_y)
    x = (s_y*g_x + s_x*g_y)/(g_y+s_y)
    print(x)
ball()
