def countC(a,b):
    result=0
    for i in range(len(a)):
        result+=b[i]-a[i]+1
    return result
