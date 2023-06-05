def main():
    s,t,x = map(int,input().split())
    if t > s:
        if x >= s and x <= t:
            print('Yes')
        else:
            print('No')
    else:
        if x >= s or x <= t:
            print('Yes')
        else:
            print('No')

if __name__ == '__main__':
    main()