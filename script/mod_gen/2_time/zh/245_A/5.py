def main():
    a,b,c,d = map(int,input().split())
    if a > c:
        print('高桥')
    elif a < c:
        print('青木')
    elif b > d:
        print('高桥')
    elif b < d:
        print('青木')
    else:
        print('同時')

if __name__ == '__main__':
    main()