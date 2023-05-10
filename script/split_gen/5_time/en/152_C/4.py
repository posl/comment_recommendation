def main():
    n = int(input())
    p = list(map(int, input().split()))
    mi = p[0]
    cnt = 1
    for i in range(1, n):
        if p[i] <= mi:
            mi = p[i]
            cnt += 1
    print(cnt)
    return
