def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        x,y = map(int,input().split())
        a.append(x)
        b.append(y)
    if a.count(a[0]) == N-1:
        print("Yes")
    elif b.count(b[0]) == N-1:
        print("Yes")
    else:
        print("No")
