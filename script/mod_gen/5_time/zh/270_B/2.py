def main():
    x,y,z = map(int,input().split())
    if x > 0 and y < 0 and z > 0:
        print(-1)
    elif x < 0 and y > 0 and z < 0:
        print(-1)
    else:
        if x < 0:
            x = -x
        if y < 0:
            y = -y
        print(x+y+z)

if __name__ == '__main__':
    main()