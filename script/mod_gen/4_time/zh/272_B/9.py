def main():
    n,m = map(int,input().split())
    a = []
    for i in range(m):
        a.append(list(map(int,input().split())))
    for i in range(m):
        for j in range(i+1,m):
            if len(set(a[i][1:]+a[j][1:])) == n:
                print("No")
                return
    print("Yes")
main()
