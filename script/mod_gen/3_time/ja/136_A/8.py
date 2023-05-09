def main():
    a,b,c = map(int,input().split())
    print(c if a >= c else a - (c - b))

if __name__ == '__main__':
    main()