def sum_of_number():
    n = int(input())
    a = input().split()
    sum = 0
    for i in range(n):
        sum += int(a[i])
    print(sum)

if __name__ == '__main__':
    sum_of_number()