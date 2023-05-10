def main():
    N = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(N):
        if a[i] < i + 1:
            continue
        else:
            count += a[i] - i - 1
    print(count)
