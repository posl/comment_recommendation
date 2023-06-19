def sum():
    n = int(input())
    num_list = list(map(int,input().split()))
    sum = 0
    for i in range(n):
        sum += num_list[i]
    print(sum)
sum()
