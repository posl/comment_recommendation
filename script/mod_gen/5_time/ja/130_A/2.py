def main():
    x,a = map(int,input().split())
    print([0,10][x>=a])

if __name__ == '__main__':
    main()