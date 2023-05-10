def main():
    n, w = map(int, input().split())
    a = list(map(int, input().split()))
    ans = 0
    for i in range(1, w + 1):
        flag = True
        for j in range(n):
            if a[j] <= i and flag:
                if i % a[j] == 0:
                    ans += 1
                    flag = False
    print(ans)
