def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = []
    for i in range(q):
        k.append(int(input()))
    a.sort()
    b = [0] * n
    for i in range(n):
        if i == 0:
            b[i] = a[i] - 1
        else:
            b[i] = a[i] - a[i-1] - 1
    for i in range(1, n):
        b[i] += b[i-1]
    # print(b)
    for i in range(q):
        if k[i] > b[-1]:
            print(a[-1] + k[i] - b[-1])
        else:
            idx = binary_search(b, k[i])
            print(a[idx] - (b[idx] - k[i] + 1))

if __name__ == '__main__':
    main()