def main():
    N = int(input())
    a = []
    b = []
    for i in range(N-1):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    a.sort()
    b.sort()
    if a[0] == 1 and b.count(1) == N-1:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()