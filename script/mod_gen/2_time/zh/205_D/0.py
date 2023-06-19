def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    a.sort()
    # print(a)
    # print(k)
    for i in range(q):
        # print(k[i])
        # print(a[k[i]-1])
        # print(a)
        # print(set(a))

if __name__ == '__main__':
    main()