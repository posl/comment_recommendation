def main():
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n-1):
        a[i],b[i] = map(int,input().split())
    a.sort()
    b.sort()
    if a[0] == 1 and b[-1] == n:
        print("Yes")
    else:
        print("No")
