def main():
    a,b,c,d = map(int,input().split())
    print(max(a*d,b*d,a*c,b*c))

if __name__ == '__main__':
    main()