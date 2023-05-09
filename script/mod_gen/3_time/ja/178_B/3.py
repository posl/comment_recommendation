def main():
    a,b,c,d = map(int, input().split())
    if 0 <= a or 0 <= c:
        print(max(a*c, a*d, b*c, b*d))
    else:
        print(max(a*d, b*c))

if __name__ == '__main__':
    main()