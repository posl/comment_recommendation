def problems243_a():
    v,a,b,c = map(int,input().split())
    #print(v,a,b,c)
    while True:
        if v < a:
            return "F"
        v -= a
        if v < b:
            return "M"
        v -= b
        if v < c:
            return "T"
        v -= c
    return "F"
print(problems243_a())

if __name__ == '__main__':
    problems243_a()