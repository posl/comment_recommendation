def main():
    a,b,w = map(int,input().split())
    w *= 1000
    max = 0
    min = 0
    for i in range(1,w+1):
        if a*i <= w <= b*i:
            min = i
            break
    for i in range(w,0,-1):
        if a*i <= w <= b*i:
            max = i
            break
    if max == 0:
        print("UNSATISFIABLE")
    else:
        print(min,max)

if __name__ == '__main__':
    main()