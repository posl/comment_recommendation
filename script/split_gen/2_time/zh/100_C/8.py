def main():
    # N = int(input())
    # a = list(map(int, input().split()))
    N = 3
    a = [5, 2, 4]
    cnt = 0
    for i in range(N):
        while a[i] % 2 == 0:
            a[i] //= 2
            cnt += 1
    print(cnt)
