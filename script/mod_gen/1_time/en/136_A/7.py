def main():
    a,b,c = map(int,input().split())
    print(a-b if a-b<c else c)

if __name__ == '__main__':
    main()