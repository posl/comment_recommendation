def main():
    a,b,c = map(int,input().split())
    print(c if c <= a - b else a - b)

if __name__ == '__main__':
    main()