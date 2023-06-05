def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 1000000000
    max = 0
    for i in range(1,1000001):
        if a*i <= w <= b*i:
            if i < min:
                min = i
            if i > max:
                max = i
    if min == 1000000000:
        print("UNSATISFIABLE")
    else:
        print(min,max)
