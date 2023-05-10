def main():
    A,B,C,D = map(int, input().split())
    x = B//C - (A-1)//C
    y = B//D - (A-1)//D
    z = B//(C*D) - (A-1)//(C*D)
    print(B-A+1-x-y+z)

if __name__ == '__main__':
    main()