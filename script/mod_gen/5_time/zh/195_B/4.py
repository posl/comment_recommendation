def main():
    a,b,w=map(int,input().split())
    w=w*1000
    min_num=0
    max_num=0
    for i in range(a,b+1):
        if w%i==0:
            if min_num==0:
                min_num=w//i
            max_num=w//i
    if min_num==0:
        print("UNSATISFIABLE")
    else:
        print(min_num,max_num)

if __name__ == '__main__':
    main()