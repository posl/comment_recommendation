def main():
    a,b,x = map(int, input().split())
    if a*b*b/2 >= x:
        print(90-(x*2)/(a*b))
    else:
        print((x*2)/(a*a*b-2*x))

if __name__ == '__main__':
    main()