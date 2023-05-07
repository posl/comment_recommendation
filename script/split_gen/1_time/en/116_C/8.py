def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(N):
        if h[i] == 0:
            continue
        ans += h[i]
        for j in range(i+1, N):
            if h[j] >= h[i]:
                h[j] = 0
            else:
                break
    print(ans)
main()
I tried to solve this problem by myself, but it was not solved. I referred to the editorial and solved it.
