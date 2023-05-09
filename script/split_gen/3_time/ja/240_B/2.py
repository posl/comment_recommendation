def main():
    N = int(input())
    a = list(map(int, input().split()))
    a.sort()
    cnt = 1
    for i in range(N-1):
        if a[i] != a[i+1]:
            cnt += 1
    print(cnt)
