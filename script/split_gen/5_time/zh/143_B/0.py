def my_sum(a_list):
    if len(a_list) == 0:
        return 0
    if len(a_list) == 1:
        return a_list[0]
    else:
        return a_list[0] + my_sum(a_list[1:])
n = int(input())
d = list(map(int, input().split()))
print(my_sum([d[i] * d[j] for i in range(len(d)) for j in range(i + 1, len(d))]))
