def main():
    x,k=map(int,input().split())
    ans=x
    for i in range(k):
        ans=(ans+5)//10*10
    print(ans)

if __name__ == '__main__':
    main()