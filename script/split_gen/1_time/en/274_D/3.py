def main():
    n,x,y = map(int, input().split())
    a = list(map(int, input().split()))
    a = [0] + a + [0]
    for i in range(1,n+1):
        if a[i] > a[i-1] + a[i+1]:
            print("No")
            return
    print("Yes")
