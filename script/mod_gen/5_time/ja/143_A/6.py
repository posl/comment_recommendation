def main():
    a,b = map(int,input().split())
    if a > b:
        print(a-b*2)
    else:
        print(0)

if __name__ == '__main__':
    main()