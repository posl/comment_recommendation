def main():
    n = int(input())
    a = list(map(int,input().split()))
    b = [0]*(n+1)
    for i in range(n):
        b[a[i]] += 1
    s = 0
    for i in range(n+1):
        s += b[i]*(b[i]-1)//2
    for i in range(n):
        print(s-(b[a[i]]-1))

if __name__ == '__main__':
    main()