def main():
    a,b = map(int, input().split())
    if (a+b) < pow(10,18):
        print('Easy')
    else:
        print('Hard')

if __name__ == '__main__':
    main()