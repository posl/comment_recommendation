def main():
    n,m = map(int, input().split())
    a = []
    b = []
    for i in range(m):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)
    if a[0] == 1 or b[0] == n:
        print("No")
    else:
        print("Yes")

if __name__ == '__main__':
    main()