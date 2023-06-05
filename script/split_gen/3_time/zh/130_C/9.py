def main():
    w,h,x,y = map(int,input().split())
    s1 = w*h/2
    s2 = x*y
    s3 = w*y
    s4 = h*x
    if s1 == s2:
        print(s1,1)
    else:
        print(s1,0)
