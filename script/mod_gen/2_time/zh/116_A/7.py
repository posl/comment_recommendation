def main():
    import math
    a,b,c = map(int,input().split())
    s = (a+b+c)/2
    area = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(int(area))

if __name__ == '__main__':
    main()