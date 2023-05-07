def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [0] * q
    for i in range(q):
        x[i] = int(input())
    a.sort()
    for i in range(q):
        print(n - bisect.bisect_left(a, x[i]))

if __name__ == '__main__':
    main()