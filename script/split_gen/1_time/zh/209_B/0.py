def main():
    n,x = map(int, input().split())
    a = list(map(int, input().split()))
    a = [a[i] - 1 if i % 2 == 1 else a[i] for i in range(n)]
    if sum(a) <= x:
        print("Yes")
    else:
        print("No")
