def main():
    a,b,c,d,e,f,x = map(int,input().split(" "))
    t = 0
    while True:
        if a > 0:
            t += b
            a -= 1
        if c > 0:
            t += d
            c -= 1
        if e > 0:
            t += f
            e -= 1
        if t >= x:
            break

if __name__ == '__main__':
    main()