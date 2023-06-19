def solve():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 1000000
    max = 0
    for i in range(a,b+1):
        if w % i == 0:
            if w // i <= max:
                max = w // i
            if w // i >= min:
                min = w // i
    if min == 1000000 or max == 0:
        print("UNSATISFIABLE")
    else:
        print(min,max)
