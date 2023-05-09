def main():
    N = int(input())
    p = [int(x) for x in input().split()]
    ans = 0
    for i in range(N):
        if p[i] == i:
            ans += 1
            if i+1 < N and p[i+1] == i+1:
                p[i+1] = p[i]
            else:
                p[i-1] = p[i]
    print(ans)
