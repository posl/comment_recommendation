def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    count = 1
    for i in range(n-1):
        if a[i] != a[i+1]:
            count += 1
    print(count)
