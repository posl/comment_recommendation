def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    for i in range(q):
        x = int(input())
        idx = binary_search(a, x)
        if idx == -1:
            print(n)
        else:
            print(n - idx)

if __name__ == '__main__':
    main()