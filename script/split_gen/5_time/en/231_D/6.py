def main():
    n, m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a = set(a)
    b = set(b)
    if len(a & b) > 0:
        print("Yes")
    else:
        print("No")
