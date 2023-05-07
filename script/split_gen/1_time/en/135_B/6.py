def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = sorted(a)
    c = 0
    d = 0
    for i in range(n):
        if a[i] != b[i]:
            c += 1
        if a[i] == b[i]:
            d += 1
    if c == 2 or c == 0:
        print("YES")
    else:
        print("NO")
main()
