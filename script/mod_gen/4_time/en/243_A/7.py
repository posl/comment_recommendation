def main():
    V,A,B,C = [int(i) for i in input().split()]
    if A >= V:
        print('F')
    elif B >= V:
        print('M')
    elif C >= V:
        print('T')
    else:
        print('M')

if __name__ == '__main__':
    main()