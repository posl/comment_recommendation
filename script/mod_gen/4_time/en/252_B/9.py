def main():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    a = sorted(a,reverse=True)
    b = sorted(b)
    for i in range(k):
        if a[i] < b[i]:
            print("Yes")
            exit()
    print("No")
main()
