def count_2(n):
    if n%2 != 0:
        return 0
    else:
        return 1 + count_2(n/2)
n = int(input())
a = list(map(int, input().split()))
print(sum([count_2(i) for i in a]))
