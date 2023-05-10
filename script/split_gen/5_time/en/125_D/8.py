def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    sum_a = sum(abs(x) for x in a)
    if a[0] < 0:
        sum_a -= 2 * a[0]
    elif a[0] == 0:
        pass
    else:
        sum_a += 2 * a[0]
    print(sum_a)
