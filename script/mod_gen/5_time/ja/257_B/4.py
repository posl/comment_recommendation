def main():
    n,k,q = map(int,input().split())
    a = list(map(int,input().split()))
    l = list(map(int,input().split()))
    ans = [0] * n
    for i in range(k):
        ans[a[i]-1] += 1
    for i in range(q):
        ans[l[i]-1] += 1
    for i in range(n):
        if ans[i] > 0:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    main()