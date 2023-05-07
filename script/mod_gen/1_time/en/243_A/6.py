def main():
    v,a,b,c = map(int, input().split())
    if a > b:
        if a > c:
            print('F')
        else:
            print('T')
    else:
        if b > c:
            print('M')
        else:
            print('T')
main()
Problem B

if __name__ == '__main__':
    main()