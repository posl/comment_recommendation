def main():
    n = int(input())
    a = []
    b = []
    for i in range(n):
        a_i, b_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
    t = 0
    for i in range(n):
        t += a[i] / b[i]
    t /= 2
    s = 0
    for i in range(n):
        s += a[i] / b[i]
        if s >= t:
            print(a[i] - (s - t) * b[i])
            break

if __name__ == '__main__':
    main()