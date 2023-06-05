def main():
    k,x = map(int,input().split())
    if k*500 >= x:
        print('是')
    else:
        print('否')

if __name__ == '__main__':
    main()