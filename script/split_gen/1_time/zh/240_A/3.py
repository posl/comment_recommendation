def judge(a,b):
    if (a==1 and b==3) or (a==2 and b==4) or (a==3 and b==5) or (a==4 and b==6) or (a==5 and b==7) or (a==6 and b==8) or (a==7 and b==9) or (a==8 and b==10):
        return True
    else:
        return False
a,b = map(int,input().split())
