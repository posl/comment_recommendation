def main():
    n = int(input())
    p = list(map(int, input().split()))
    cnt = 0
    min = n + 1
    for i in range(n):
        if p[i] < min:
            cnt += 1
            min = p[i]
    print(cnt)
