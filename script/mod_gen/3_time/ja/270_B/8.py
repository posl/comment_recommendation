def main():
    x,y,z = map(int,input().split())
    if z > 0:
        if y > 0:
            if x > 0:
                if x < y:
                    print(y - x)
                else:
                    print(-1)
            else:
                print(y - x)
        else:
            if x > 0:
                print(y - x)
            else:
                if x > y:
                    print(y - x)
                else:
                    print(-1)
    else:
        print(-1)

if __name__ == '__main__':
    main()