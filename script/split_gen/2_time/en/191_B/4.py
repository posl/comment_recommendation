def main():
    n,x = map(int,input().split())
    a = list(map(int,input().split()))
    for i in range(n):
        if a[i] == x:
            a[i] = 0
    for i in range(n):
        if a[i] != 0:
            print(a[i],end=" ")
