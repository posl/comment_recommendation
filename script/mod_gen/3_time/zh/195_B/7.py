def main():
    a,b,w = map(int,input().split())
    w *= 1000
    min = 1000000
    max = 0
    for i in range(1,w+1):
        if a <= i <= b:
            if min > i:
                min = i
            if max < i:
                max = i
    if min == 1000000:
        print('UNSATISFIABLE')
    else:
        print(min//1000,max//1000)

if __name__ == '__main__':
    main()