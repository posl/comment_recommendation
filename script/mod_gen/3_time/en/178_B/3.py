def main():
    a,b,c,d = map(int, input().split())
    max = a*c
    if a*d > max:
        max = a*d
    if b*c > max:
        max = b*c
    if b*d > max:
        max = b*d
    print(max)

if __name__ == '__main__':
    main()