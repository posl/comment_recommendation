def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    sum = 0
    for i in range(n):
        sum += (b[i] - a[i] + 1) * (a[i] + b[i]) / 2
    print(int(sum))

if __name__ == '__main__':
    main()