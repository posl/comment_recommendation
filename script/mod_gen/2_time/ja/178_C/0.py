def main():
    N = int(input())
    print((pow(10,N,1000000007)-pow(9,N,1000000007)-pow(9,N,1000000007)+pow(8,N,1000000007))%1000000007)

if __name__ == '__main__':
    main()