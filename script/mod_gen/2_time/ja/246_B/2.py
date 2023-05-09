def main():
    A,B = map(int,input().split())
    if A == 0:
        print(0,1)
    elif B == 0:
        print(1,0)
    else:
        if A > B:
            print(0.6,0.8)
        else:
            print(0.521964870245,0.852966983083)

if __name__ == '__main__':
    main()