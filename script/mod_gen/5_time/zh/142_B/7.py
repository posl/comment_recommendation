def main():
    n,k=map(int,input().split())
    h=list(map(int,input().split()))
    count=0
    for i in range(len(h)):
        if h[i]>=k:
            count+=1
    print(count)

if __name__ == '__main__':
    main()