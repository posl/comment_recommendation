def main():
    n = int(input())
    a = list(map(int, input().split()))
    max = 0
    count = 0
    for i in range(n):
        if a[i] >= max:
            count += 1
            max = a[i]
    print(count)
