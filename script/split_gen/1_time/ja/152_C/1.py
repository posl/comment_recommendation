def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 1
    min_p = p[0]
    for i in range(1, n):
        if p[i] <= min_p:
            cnt += 1
            min_p = p[i]
    print(cnt)
