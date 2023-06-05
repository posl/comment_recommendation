def main():
    n,k = map(int,input().split())
    result = 0
    for i in range(1,n+1):
        for j in range(1,k+1):
            result += i*100+j
    print(result)

if __name__ == '__main__':
    main()