def main():
    a,b = map(int,input().split())
    if a+b >= 10**10:
        print('Hard')
    else:
        print('Easy')
    return

if __name__ == '__main__':
    main()