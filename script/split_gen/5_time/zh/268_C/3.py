def main():
    n = int(input())
    p = list(map(int, input().split()))
    p = [i - 1 for i in p]
    cnt = 0
    for i in range(n):
        if p[p[i]] == i:
            cnt += 1
    print(cnt // 2)
