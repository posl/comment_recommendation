def main():
    n,m = map(int,input().split())
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i],b[i] = map(int,input().split())
    a = sorted(a)
    b = sorted(b)
    if a[m-1] > b[0]:
        print("No")
    else:
        print("Yes")
