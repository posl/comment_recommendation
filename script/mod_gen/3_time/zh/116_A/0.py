def main():
    import sys
    import math
    for line in sys.stdin:
        a,b,c = map(int,line.split())
        s = (a+b+c)/2
        print(int(math.sqrt(s*(s-a)*(s-b)*(s-c))))

if __name__ == '__main__':
    main()