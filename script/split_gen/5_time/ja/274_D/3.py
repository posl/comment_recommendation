def main():
    n,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n-1):
        if a[i] + a[i+1] > x:
            print("No")
            exit()
    if a[0] > y:
        print("No")
        exit()
    print("Yes")
