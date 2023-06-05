def count_square(h,w,r,c):
    count=0
    if r==1 and c==1:
        count=0
    elif r==1 and c==w:
        count=0
    elif r==h and c==1:
        count=0
    elif r==h and c==w:
        count=0
    elif r==1 and c!=1 and c!=w:
        count=1
    elif r==h and c!=1 and c!=w:
        count=1
    elif c==1 and r!=1 and r!=h:
        count=1
    elif c==w and r!=1 and r!=h:
        count=1
    else:
        count=2
    return count

if __name__ == '__main__':
    count_square()