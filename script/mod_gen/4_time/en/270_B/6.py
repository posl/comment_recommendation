def main():
    x,y,z = map(int, input().split())
    if x > z and y < z:
        print(abs(x-z)+abs(y-z)+1)
    else:
        print(-1)

if __name__ == '__main__':
    main()