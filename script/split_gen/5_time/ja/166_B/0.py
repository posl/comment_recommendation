def main():
    n, k = map(int, input().split())
    d = [0] * k
    a = [0] * k
    for i in range(k):
        d[i] = int(input())
        a[i] = list(map(int, input().split()))
    ans = 0
    for i in range(1, n+1):
        flag = True
        for j in range(k):
            if i in a[j]:
                flag = False
        if flag:
            ans += 1
    print(ans)
