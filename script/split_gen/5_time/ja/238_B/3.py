def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(reverse=True)
    a.append(a[0])
    max = 0
    for i in range(n):
        if max < (a[i] - a[i+1] + 360) % 360:
            max = (a[i] - a[i+1] + 360) % 360
    print(max)
