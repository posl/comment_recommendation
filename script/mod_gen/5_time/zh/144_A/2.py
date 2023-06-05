def main():
    a,b = map(int,input().split())
    if a <= 20 and b <= 20:
        print(a*b)
    else:
        print(-1)

if __name__ == '__main__':
    main()