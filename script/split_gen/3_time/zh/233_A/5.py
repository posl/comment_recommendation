def main():
    x,y=map(int,input().split())
    c=0
    while x<y:
        x+=10
        c+=1
    print(c)
