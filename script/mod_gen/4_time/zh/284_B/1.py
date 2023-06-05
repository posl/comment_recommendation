def count_odd_num(arr):
    count = 0
    for i in arr:
        if i%2 == 1:
            count += 1
    return count
T = int(input())
for i in range(T):
    N = int(input())
    arr = list(map(int, input().split()))
    print(count_odd_num(arr))
