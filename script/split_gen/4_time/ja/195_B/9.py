def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(1,w//a+1):
        if w == a*i:
            if min == 0:
                min = i
            max = i
        if a*i < w and w <= b*i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min,max)
