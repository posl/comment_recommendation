def main():
    n = int(input())
    p = list(map(int, input().split()))
    min = n+1
    cnt = 0
    for i in range(n):
        if p[i] < min:
            cnt += 1
            min = p[i]
    print(cnt)
