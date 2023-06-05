def main():
    n, k = map(int, input().split())
    d = []
    a = []
    for i in range(k):
        d.append(int(input()))
        a.append(list(map(int, input().split())))
    cnt = 0
    for i in range(n):
        for j in range(k):
            if i+1 in a[j]:
                break
        else:
            cnt += 1
    print(cnt)
