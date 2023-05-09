def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N):
        if a[i] == 1:
            ans.append(i+1)
    if len(ans) % 2 == 0:
        print(len(ans))
        print(*ans)
    else:
        print(-1)
