def main():
    n, x = map(int, input().split())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    pos = 0
    for i in range(n):
        if i % 2 == 0:
            pos += a[i]
        else:
            pos += b[i]
    if pos == x:
        print("Yes")
    else:
        print("No")
