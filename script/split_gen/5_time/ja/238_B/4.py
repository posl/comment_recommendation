def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    sum = 0
    for i in range(n):
        if i % 2 == 0:
            sum += a[i]
        else:
            sum -= a[i]
    print(sum)
