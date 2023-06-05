def main():
    n=int(input())
    d=[int(i) for i in input().split()]
    d.sort()
    count=0
    for i in range(n//2,n):
        if d[i]>d[i-1]:
            count+=1
    print(count)

if __name__ == '__main__':
    main()