def f(x1,y1,x2,y2):
    if x1==x2 or y1==y2:
        return "No"
    if abs(x1-x2)==abs(y1-y2):
        return "Yes"
    else:
        return "No"
x1,y1,x2,y2=map(int,input().split())
print(f(x1,y1,x2,y2))
