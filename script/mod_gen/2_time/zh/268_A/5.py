def main():
    a,b,c,d,e = map(int, input().split())
    print(len({a,b,c,d,e}))

if __name__ == '__main__':
    main()