def main():
    a,b = map(int,input().split())
    a = sum(list(map(int,str(a))))
    b = sum(list(map(int,str(b))))
    print(a if a>b else b)

if __name__ == '__main__':
    main()