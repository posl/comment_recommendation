def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min_d = 100000000
    min_i = 0
    for i in range(n):
        d = abs(a - (t - h[i] * 0.006))
        if min_d > d:
            min_d = d
            min_i = i
    print(min_i + 1)

if __name__ == '__main__':
    main()