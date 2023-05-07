def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = list(map(int, input().split()))
    for i in range(q):
        print(bisect.bisect_left(a, x[i]))

if __name__ == '__main__':
    main()