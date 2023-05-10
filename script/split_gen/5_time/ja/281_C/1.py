def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    a = a * 2
    sum = 0
    for i in range(len(a)):
        sum += a[i]
        if sum >= t:
            print(i + 1, t - (sum - a[i]))
            break
