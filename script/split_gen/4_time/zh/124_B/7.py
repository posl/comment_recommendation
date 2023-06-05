def main():
    n = int(input())
    h = list(map(int, input().split()))
    cnt = 1
    for i in range(1, n):
        for j in range(i):
            if h[i] < h[j]:
                break
        else:
            cnt += 1
    print(cnt)
