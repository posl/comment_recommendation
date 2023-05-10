def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        ai, bi = map(int, input().split())
        a.append(ai)
        b.append(bi)
    count = 0
    for i in range(n):
        count += a[i]
        if count > x:
            print("No")
            exit()
        count += b[i]
    if count <= x:
        print("Yes")
    else:
        print("No")
