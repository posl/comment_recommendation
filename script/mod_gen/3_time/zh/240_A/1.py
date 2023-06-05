def judge(a,b):
    if a>b:
        a,b=b,a
    if a==1 and b==2:
        return True
    if a==2 and b==4:
        return True
    if a==3 and b==4:
        return True
    if a==4 and b==5:
        return True
    if a==5 and b==7:
        return True
    if a==6 and b==7:
        return True
    if a==7 and b==8:
        return True
    if a==8 and b==9:
        return True
    if a==9 and b==10:
        return True
    return False

if __name__ == '__main__':
    judge()