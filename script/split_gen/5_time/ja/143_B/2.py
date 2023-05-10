def sum_of_combination(num):
    sum = 0
    for i in range(num):
        for j in range(i+1,num):
            sum += d[i] * d[j]
    return sum
n = int(input())
d = list(map(int,input().split()))
print(sum_of_combination(n))
