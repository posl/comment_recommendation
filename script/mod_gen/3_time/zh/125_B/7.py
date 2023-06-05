def main():
    n = int(input())
    v = list(map(int, input().split()))
    c = list(map(int, input().split()))
    max = 0
    for i in range(1, 2**n):
        sum_v = 0
        sum_c = 0
        for j in range(n):
            if (i >> j) & 1:
                sum_v += v[j]
                sum_c += c[j]
        if sum_v - sum_c > max:
            max = sum_v - sum_c
    print(max)

if __name__ == '__main__':
    main()