def count_odd():
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] % 2 == 1:
            cnt += 1
    print(cnt)
t = int(input())
for i in range(t):
    count_odd()
