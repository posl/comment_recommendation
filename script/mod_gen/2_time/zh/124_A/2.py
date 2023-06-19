def main():
    a,b = map(int,input().split())
    if a == b:
        print(a + b)
    else:
        print(max(a,b)*2-1)

if __name__ == '__main__':
    main()