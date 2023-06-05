def main():
    #n,k=[int(i) for i in input().split()]
    n,k=map(int,input().split())
    print(0 if n%k==0 else 1)

if __name__ == '__main__':
    main()