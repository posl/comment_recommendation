def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min_num = min(a,b,c,d,e)
    if min_num < n:
        print(5 + (n-1)//min_num)
    else:
        print(5)

if __name__ == '__main__':
    main()