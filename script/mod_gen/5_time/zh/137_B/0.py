def main():
    k,x = map(int,input().split())
    if k == 1:
        print(x)
    else:
        for i in range(x-k+1,x+k):
            print(i,end=' ')

if __name__ == '__main__':
    main()