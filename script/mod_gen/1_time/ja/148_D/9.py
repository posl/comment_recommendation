def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    if max(a) > n:
        print("-1")
        return
    b = [0] * n
    for i in range(n):
        b[a[i]-1] += 1
    print(n - max(b))

if __name__ == '__main__':
    main()