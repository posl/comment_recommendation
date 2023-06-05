def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 1000000
    max = 0
    for i in range(a,b+1):
        if i <= w and w <= i*b:
            if i < min:
                min = i
            if i > max:
                max = i
    if min == 1000000:
        print("UNSATISFIABLE")
    else:
        print(min,max)
