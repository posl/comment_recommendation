def main():
    N, C = map(int, input().split())
    a = []
    b = []
    c = []
    for i in range(N):
        a_i, b_i, c_i = map(int, input().split())
        a.append(a_i)
        b.append(b_i)
        c.append(c_i)
    a.sort()
    b.sort()
    c.sort()
    total = 0
    i = 0
    j = 0
    k = 0
    while i < N:
        while j < N and a[j] <= b[i]:
            j += 1
        total += C * (j - k)
        k = j
        while k < N and b[k] < a[i]:
            k += 1
        total += c[i] * (k - j)
        i += 1
    print(total)

if __name__ == '__main__':
    main()