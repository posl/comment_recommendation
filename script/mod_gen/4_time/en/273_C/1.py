def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    a.append(-1)
    ans = [0] * n
    cnt = 1
    for i in range(n):
        if a[i] == a[i+1]:
            cnt += 1
        else:
            ans[cnt-1] += 1
            cnt = 1
    for i in range(n):
        print(ans[i])
main()
