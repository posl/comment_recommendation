def main():
    x,y,z = map(int,input().split())
    if y*z > 0:
        if abs(x) > abs(y):
            print(abs(x-y))
        else:
            print(abs(y-x))
    else:
        print(-1)

if __name__ == '__main__':
    main()