def main():
    N = int(input())
    a = list(map(int, input().split()))
    if sum(a) == 0:
        print(0)
        return
    if sum(a) % 2 == 1:
        print(-1)
        return
    ans = []
    for i in range(N):
        if a[i] == 1:
            ans.append(i+1)
    print(len(ans))
    print(*ans)
