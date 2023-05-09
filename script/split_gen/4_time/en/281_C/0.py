def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(n):
        sum += a[i]
        if sum >= t:
            print(i+1, t-(sum-a[i-1]))
            break
