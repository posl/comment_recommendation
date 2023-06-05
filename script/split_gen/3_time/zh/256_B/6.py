def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        cnt += a[i] - 1
    print(cnt)
