def main():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] == i+1:
            cnt += 1
    for i in range(n-1):
        if a[i] == i+1:
            if a[i+1] == i+2:
                cnt += 1
    print(cnt)
