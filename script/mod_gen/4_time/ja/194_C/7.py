def main():
    n = int(input())
    a = list(map(int,input().split()))
    print(sum([sum([(a[i]-a[j])**2 for j in range(i)]) for i in range(1,n)]))

if __name__ == '__main__':
    main()