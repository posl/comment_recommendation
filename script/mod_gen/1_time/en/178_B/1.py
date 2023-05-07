def main():
    a,b,c,d = map(int, input().split())
    l = [a*c, a*d, b*c, b*d]
    print(max(l))
main()

if __name__ == '__main__':
    main()