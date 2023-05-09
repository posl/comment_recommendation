def main():
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(n//2):
        if a[i] != a[n-i-1]:
            count += 1
    print(count)
