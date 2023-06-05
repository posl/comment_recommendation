def pow(a,b):
    if a==0:
        return 0
    if b==0:
        return 1
    if b==1:
        return a
    if b<0:
        return 1/pow(a,-b)
    if b%2==0:
        return pow(a,b/2)*pow(a,b/2)
    else:
        return pow(a,(b-1)/2)*pow(a,(b-1)/2)*a
