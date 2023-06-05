def isYes(n,x,y,a):
    if n<=2:
        return "Yes"
    if x==0 and y==0:
        return "Yes"
    if n==3:
        if a[0]==a[1] and a[1]==a[2]:
            return "Yes"
        else:
            return "No"
    if n==4:
        if a[0]==a[1] and a[2]==a[3]:
            return "Yes"
        else:
            return "No"
    if n==5:
        if a[0]==a[1] and a[1]==a[2] and a[2]==a[3] and a[3]==a[4]:
            return "Yes"
        else:
            return "No"
    if n==6:
        if a[0]==a[1] and a[1]==a[2] and a[2]==a[3] and a[3]==a[4] and a[4]==a[5]:
            return "Yes"
        else:
            return "No"
    if n==7:
        if a[0]==a[1] and a[1]==a[2] and a[2]==a[3] and a[3]==a[4] and a[4]==a[5] and a[5]==a[6]:
            return "Yes"
        else:
            return "No"
    if n==8:
        if a[0]==a[1] and a[1]==a[2] and a[2]==a[3] and a[3]==a[4] and a[4]==a[5] and a[5]==a[6] and a[6]==a[7]:
            return "Yes"
        else:
            return "No"
    if n==9:
        if a[0]==a[1] and a[1]==a[2] and a[2]==a[3] and a[3]==a[4] and a[4]==a[5] and a[5]==a[6] and a[6]==a[7] and a[7]==a[8]:
            return "Yes"
        else:
            return "No"
    if n==10:
        if a[0]==a[1] and a[1]==

if __name__ == '__main__':
    isYes()