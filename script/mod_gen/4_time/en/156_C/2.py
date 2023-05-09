def main():
    n = int(input())
    x = list(map(int, input().split()))
    min_x = min(x)
    max_x = max(x)
    min_sum = 1000000000
    for i in range(min_x,max_x+1):
        tmp_sum = 0
        for j in range(n):
            tmp_sum += (x[j]-i)**2
        if tmp_sum < min_sum:
            min_sum = tmp_sum
    print(min_sum)

if __name__ == '__main__':
    main()