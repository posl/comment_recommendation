def main():
    # a,b,c = map(int,input().split())
    # print(a+b+c-max(a,b,c))
    a = list(map(int,input().split()))
    print(sum(a)-max(a))

if __name__ == '__main__':
    main()