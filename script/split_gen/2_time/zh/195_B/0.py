def main():
    a,b,w = map(int,input().split())
    w = w*1000
    # print(a,b,w)
    min = 0
    max = 0
    for i in range(1,w+1):
        # print(i)
        if a*i <= w and w <= b*i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print("UNSATISFIABLE")
    else:
        print(min,max)
