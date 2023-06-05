def calc(x):
    if x < 10:
        return 0
    else:
        return x - 10
n = int(input())
a = list(map(int,input().split()))
print(sum(map(calc,a)))
