def time(k):
    h = k//60
    m = k%60
    if h<10:
        h = '0'+str(h)
    else:
        h = str(h)
    if m<10:
        m = '0'+str(m)
    else:
        m = str(m)
    return h+':'+m
k = int(input())
print(time(k))
