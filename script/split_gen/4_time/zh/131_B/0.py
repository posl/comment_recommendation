def main():
    n, l = map(int, input().split())
    sum = 0
    for i in range(1, n+1):
        sum += l + i - 1
    if l + n - 1 > 0:
        sum -= l + n - 1
    elif l < 0:
        sum -= l
    print(sum)
