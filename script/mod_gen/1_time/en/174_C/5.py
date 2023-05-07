def main():
    #input
    K = int(input())
    #compute
    if K%2==0 or K%5==0:
        print(-1)
        return
    i = 1
    while i%K!=0:
        i = 10*i+7
        i %= K
    #output
    print(i+1)

if __name__ == '__main__':
    main()