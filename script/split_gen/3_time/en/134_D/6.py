def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(n):
        if a[n-1-i] == 1:
            ans.append(n-i)
            for j in range(1, n//ans[-1]+1):
                a[ans[-1]*j-1] = 1 - a[ans[-1]*j-1]
    print(len(ans))
    print(*ans)
