def main():
    a,b,x = map(int, input().split())
    if x <= a*a*b/2:
        print(90 - (x/a/a*2)*90)
    else:
        print((2*(a*a*b-x)/a/a/a)*90)

if __name__ == '__main__':
    main()