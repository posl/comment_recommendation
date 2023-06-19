def main():
    a, b, x = map(int, input().split())
    if x <= a*a*b/2:
        print(90 - 2*x/a/a/b*180)
    else:
        print(2*(a*a*b-x)/a/a/a*180)

if __name__ == '__main__':
    main()