def get_line(x1,y1,x2,y2):
    if x1==x2:
        return 'x='+str(x1)
    elif y1==y2:
        return 'y='+str(y1)
    else:
        k=(y1-y2)/(x1-x2)
        b=y1-k*x1
        return 'y='+str(k)+'x+'+str(b)

if __name__ == '__main__':
    get_line()