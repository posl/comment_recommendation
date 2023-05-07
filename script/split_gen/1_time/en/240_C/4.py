def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    for i in range(n):
        x -= a[i]
        if x < 0:
            print("No")
            return
        x += b[i]
    if x < 0:
        print("No")
    else:
        print("Yes")
    return
