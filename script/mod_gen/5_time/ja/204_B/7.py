def harvest(n, a_list):
    count = 0
    for i in range(n):
        if a_list[i] > 10:
            count += a_list[i] - 10
    return count
n = int(input())
a_list = list(map(int, input().split()))
print(harvest(n, a_list))
