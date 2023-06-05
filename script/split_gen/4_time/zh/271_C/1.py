def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 0
    for i in range(n):
        if a[i] > count + 1:
            break
        else:
            count += a[i]
    print(count + 1)
