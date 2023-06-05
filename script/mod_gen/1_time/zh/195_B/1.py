def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 0
    max = 0
    for i in range(a,b+1):
        if w%i == 0:
            min = w//i
            break
    for i in range(b,a-1,-1):
        if w%i == 0:
            max = w//i
            break
    if min == 0 and max == 0:
        print('UNSATISFIABLE')
    else:
        print(min,max)

if __name__ == '__main__':
    main()