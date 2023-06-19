def main():
    a,b,c,d,e,f,x = map(int,input().split())
    t = 0
    while x > 0:
        if a > 0:
            x -= b
            t += a
        if x > 0:
            x -= d
            t += c
        if x > 0:
            x -= e
            t += f
    if a > d:
        print('高桥')
    elif a < d:
        print('青木')
    else:
        print('画')

if __name__ == '__main__':
    main()