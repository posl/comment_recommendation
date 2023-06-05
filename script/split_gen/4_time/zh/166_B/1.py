def main():
    n, k = map(int, input().split())
    d = [0 for i in range(k)]
    a = [[0 for i in range(n)] for j in range(k)]
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        flag = False
        for j in range(k):
            if i+1 in a[j]:
                flag = True
        if not flag:
            cnt += 1
    print(cnt)
