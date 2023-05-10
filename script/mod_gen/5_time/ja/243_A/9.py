def main():
    V,A,B,C = map(int,input().split())
    while True:
        if V - A < 0:
            print('T')
            break
        V = V - A
        if V - B < 0:
            print('F')
            break
        V = V - B
        if V - C < 0:
            print('M')
            break
        V = V - C

if __name__ == '__main__':
    main()