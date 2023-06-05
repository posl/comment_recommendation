def isConfuseTime(h,m):
    if h==0:
        h=24
    if h<10:
        h=str(h)
        h='0'+h
    if m<10:
        m=str(m)
        m='0'+m
    if h[1]==m[0] and h[0]==m[1]:
        return True
    else:
        return False

if __name__ == '__main__':
    isConfuseTime()