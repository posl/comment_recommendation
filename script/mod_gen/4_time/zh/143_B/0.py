def main():
    n = int(input())
    d = list(map(int, input().split()))
    sum_d = 0
    for i in range(n):
        sum_d += d[i]
    sum_d = sum_d**2
    sum_d2 = 0
    for i in range(n):
        sum_d2 += d[i]**2
    print((sum_d-sum_d2)//2)

if __name__ == '__main__':
    main()