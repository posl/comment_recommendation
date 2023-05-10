def resolve():
    import math
    a,b,w = map(int, input().split())
    w = w * 1000
    max = math.floor(w/a)
    min = math.ceil(w/b)
    if max < min:
        print("UNSATISFIABLE")
    else:
        print(min,max)
    return
