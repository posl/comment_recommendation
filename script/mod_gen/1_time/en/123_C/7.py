def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())
    min_time = min(a,b,c,d,e)
    print((n-1)//min_time + 5)

if __name__ == '__main__':
    main()