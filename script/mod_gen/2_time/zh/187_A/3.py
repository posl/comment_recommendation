def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    # 1. 两两之差
    # 2. 两两之差的和
    # 3. 两两之差的和的和
    # 4. 两两之差的和的和的和
    # 5. 两两之差的和的和的和的和
    # 1. 两两之差
    diff = []
    for i in range(n):
        for j in range(i+1, n):
            diff.append(abs(a[i] - a[j]))
    # 2. 两两之差的和
    diff_sum = 0
    for i in range(len(diff)):
        diff_sum += diff[i]
    # 3. 两两之差的和的和
    diff_sum_sum = 0
    for i in range(len(diff)):
        diff_sum_sum += diff_sum
    # 4. 两两之差的和的和的和
    diff_sum_sum_sum = 0
    for i in range(len(diff)):
        diff_sum_sum_sum += diff_sum_sum
    # 5. 两两之差的和的和的和的和
    diff_sum_sum_sum_sum = 0
    for i in range(len(diff)):
        diff_sum_sum_sum_sum += diff_sum_sum_sum
    print(diff_sum_sum_sum_sum)

if __name__ == '__main__':
    main()