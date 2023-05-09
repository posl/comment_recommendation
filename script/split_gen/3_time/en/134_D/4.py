def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N):
        if a[N-i-1] == 1:
            ans.append(N-i)
            for j in range(1, N//ans[-1]+1):
                a[ans[-1]*j-1] = 1 - a[ans[-1]*j-1]
    print(len(ans))
    for i in range(len(ans)):
        print(ans[len(ans)-i-1], end=' ')
    print()
