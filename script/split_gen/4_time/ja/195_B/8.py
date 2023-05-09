def solve():
    a,b,w = map(int, input().split())
    w *= 1000
    min = 1000000000
    max = 0
    for i in range(1,1000001):
        if a <= w / i and w / i <= b:
            if min > i:
                min = i
            if max < i:
                max = i
    if max == 0:
        print("UNSATISFIABLE")
    else:
        print(min, max)
