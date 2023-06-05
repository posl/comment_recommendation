def main():
    x,y,z = map(int,input().split())
    if (x > y and y > z) or (x < y and y < z):
        print(-1)
    else:
        print(abs(x-z)+abs(y-z))

if __name__ == '__main__':
    main()