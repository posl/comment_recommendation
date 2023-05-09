def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(0, n-1):
        for j in range(i+1, n):
            if (a[i] - a[j]) % 200 == 0:
                count += 1
    print(count)
