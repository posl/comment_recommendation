def cut(x,y,w,h):
    if x==w/2 and y==h/2:
        return w*h/2
    elif x==w/2:
        return h*x
    elif y==h/2:
        return w*y
    elif x==0 and y==0:
        return w*h/2
    elif x==0:
        return w*h/2
    elif y==0:
        return w*h/2
    else:
        return max(x*h,(w-x)*h,w*y,w*(h-y))
