def main():
    import sys
    from math import sqrt
    readline = sys.stdin.buffer.readline
    #read = sys.stdin.buffer.read
    #readlines = sys.stdin.buffer.readlines
    r,x,y = map(int,readline().split())
    d = sqrt(x**2+y**2)
    if d < r:
        print(2)
    else:
        print(int(d//r)+1)

if __name__ == '__main__':
    main()