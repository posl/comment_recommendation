def problems243_a():
    v,a,b,c = map(int,input().split())
    if v <= 0 or v > 100000:
        return
    if a <= 0 or a > 100000:
        return
    if b <= 0 or b > 100000:
        return
    if c <= 0 or c > 100000:
        return
    if v < a:
        return
    if v < b:
        return
    if v < c:
        return
    while v >= 0:
        v -= a
        if v < 0:
            return "F"
        v -= b
        if v < 0:
            return "M"
        v -= c
        if v < 0:
            return "T"
print(problems243_a())

if __name__ == '__main__':
    problems243_a()