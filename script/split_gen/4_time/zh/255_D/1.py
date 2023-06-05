def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    x = [int(input()) for _ in range(q)]
    sum = 0
    for i in range(1, n):
        sum += abs(a[i] - a[i - 1])
    for i in range(q):
        if x[i] == a[0]:
            sum += abs(a[1] - a[0])
            sum -= abs(a[1] - a[0] + a[0] - x[i])
            a[0] = x[i]
        elif x[i] == a[-1]:
            sum += abs(a[-2] - a[-1])
            sum -= abs(a[-2] - a[-1] + a[-1] - x[i])
            a[-1] = x[i]
        else:
            for j in range(1, n - 1):
                if x[i] == a[j]:
                    sum += abs(a[j - 1] - a[j])
                    sum += abs(a[j + 1] - a[j])
                    sum -= abs(a[j - 1] - a[j] + a[j] - x[i])
                    sum -= abs(a[j + 1] - a[j] + a[j] - x[i])
                    a[j] = x[i]
        print(sum)
