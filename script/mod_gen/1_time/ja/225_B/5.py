def main():
    n = int(input())
    a = [0 for i in range(n)]
    for i in range(n-1):
        x,y = map(int,input().split())
        a[x-1] += 1
        a[y-1] += 1
    if max(a) == n-1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()