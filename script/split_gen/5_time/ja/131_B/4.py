def main():
    n, l = map(int, input().split())
    sum = 0
    min = 10000000
    for i in range(n):
        sum += l + i
        if min > abs(l + i):
            min = abs(l + i)
    print(sum - min)
