def main():
    n = int(input())
    a = []
    b = []
    for i in range(n-1):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a.sort()
    b.sort()
    if a[0] == 1:
        if a[1:] == b[1:]:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
