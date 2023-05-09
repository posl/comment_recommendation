def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(a[i][1]):
            b.append(a[i][0])
    if sum(b) == x:
        print("Yes")
    else:
        print("No")
