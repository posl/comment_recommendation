def main():
    n = int(input())
    a = [0] * (n - 1)
    b = [0] * (n - 1)
    for i in range(n - 1):
        a[i], b[i] = map(int, input().split())
    a.sort()
    b.sort()
    if a[0] == 1 and b[0] == n:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()