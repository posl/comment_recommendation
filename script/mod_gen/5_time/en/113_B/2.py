def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    min = 10000000
    min_index = 0
    for i in range(n):
        if abs(a - (t - h[i] * 0.006)) < min:
            min = abs(a - (t - h[i] * 0.006))
            min_index = i + 1
    print(min_index)

if __name__ == '__main__':
    main()