def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.append(0)
    a.append(360)
    a.sort()
    max = 0
    for i in range(1, n+1):
        diff = a[i] - a[i-1]
        if diff > max:
            max = diff
    print(360 - max)
