def main():
    a,b,k = map(int,input().split())
    if k <= a:
        print(a-k,b)
    else:
        print(0,max(0,b-(k-a)))

if __name__ == '__main__':
    main()