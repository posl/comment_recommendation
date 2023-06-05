def main():
    a,b = map(int,input().split())
    print(a/(a**2+b**2)**0.5,b/(a**2+b**2)**0.5)

if __name__ == '__main__':
    main()