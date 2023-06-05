def main():
    n,k,q = map(int,input().split())
    a = [int(input()) for i in range(q)]
    p = [0 for i in range(n)]
    for i in range(q):
        p[a[i]-1] += 1
    for i in range(n):
        if k + p[i] - q > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()