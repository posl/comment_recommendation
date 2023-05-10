def count_average(n, a):
    count = 0
    for i in range(1, 2**n):
        sum = 0
        for j in range(n):
            if i & (1 << j) != 0:
                sum += a[j]
        if sum % len(bin(i)[2:]) == 0:
            count += 1
    return count
n = int(input())
a = list(map(int, input().split()))
print(count_average(n, a))

if __name__ == '__main__':
    count_average()