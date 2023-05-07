def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    k = [int(input()) for _ in range(q)]
    for i in k:
        print(a[i-1])

if __name__ == '__main__':
    main()