def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N):
        a[i] -= 1
        ans.append(a[i])
        if i > 0:
            ans[i] += ans[i-1]
            if a[i-1] == 1:
                ans[i] -= 1
                a[i] = 0
    print(*ans, sep='\n')
