def main():
    v,a,b,c = map(int, input().split())
    if a > b:
        if b > c:
            print('F')
        else:
            print('M')
    else:
        if a > c:
            print('F')
        else:
            print('T')

if __name__ == '__main__':
    main()