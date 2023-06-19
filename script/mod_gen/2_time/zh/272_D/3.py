def main():
    n,m = map(int,input().split())
    for i in range(n):
        for j in range(n):
            if i==j:
                print(0,end=' ')
            else:
                print(1,end=' ')
        print()

if __name__ == '__main__':
    main()