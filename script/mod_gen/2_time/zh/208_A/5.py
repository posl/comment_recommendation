def main():
    A,B = map(int,input().split())
    if A*6 >= B and A <= B:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()