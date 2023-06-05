def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(1,1001):
        if a*i <= w <= b*i:
            if min == 0:
                min = i
            max = i
    if min == 0:
        print('UNSATISFIABLE')
    else:
        print(min,max)

if __name__ == '__main__':
    main()