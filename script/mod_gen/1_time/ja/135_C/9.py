def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    max_kill = 0
    for i in range(n):
        if a[i] >= b[i]:
            max_kill += b[i]
        else:
            max_kill += a[i]
            b[i] -= a[i]
            if a[i+1] >= b[i]:
                max_kill += b[i]
                a[i+1] -= b[i]
            else:
                max_kill += a[i+1]
                a[i+1] = 0
    print(max_kill)

if __name__ == '__main__':
    main()