def problems243_a():
    v,a,b,c = map(int, input().split())
    while v > 0:
        if v < a:
            print("F")
            break
        v -= a
        if v < b:
            print("M")
            break
        v -= b
        if v < c:
            print("T")
            break
        v -= c

if __name__ == '__main__':
    problems243_a()