def main():
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    for i in range(q):
        x = list(map(int, input().split()))
        if x[0] == 1:
            for j in range(n):
                a[j] = x[1]
        elif x[0] == 2:
            a[x[1] - 1] += x[2]
        else:
            print(a[x[1] - 1])

if __name__ == '__main__':
    main()