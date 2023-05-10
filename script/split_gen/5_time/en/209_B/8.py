def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [a[i] for i in range(0, n, 2)]
    if sum(a) <= x:
        print("Yes")
    else:
        print("No")
