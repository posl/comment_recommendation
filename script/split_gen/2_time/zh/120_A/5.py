def search(a,b,query):
    a = list(map(int, a))
    b = list(map(int, b))
    query = list(map(int, query))
    result = []
    for q in query:
        a.append(q)
        b.append(q)
        a.sort()
        b.sort()
        aindex = a.index(q)
        bindex = b.index(q)
        if aindex == 0:
            amin = a[aindex]
        else:
            amin = q - a[aindex-1]
        if bindex == 0:
            bmin = b[bindex]
        else:
            bmin = q - b[bindex-1]
        result.append(min(amin,bmin))
    return result
