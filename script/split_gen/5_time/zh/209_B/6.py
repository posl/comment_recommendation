def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [a[i] if i%2==0 else a[i]-1 for i in range(n)]
    if sum(a) <= x:
        print("Yes")
    else:
        print("No")
