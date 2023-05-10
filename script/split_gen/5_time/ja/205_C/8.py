def pow(a,b):
    if(b==0):
        return 1
    else:
        return a*pow(a,b-1)
a,b,c=map(int,input().split())
if(pow(a,c)<pow(b,c)):
    print("<")
elif(pow(a,c)>pow(b,c)):
    print(">")
else:
    print("=")
