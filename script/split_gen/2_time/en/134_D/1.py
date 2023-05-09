def main():
    N = int(input())
    a = list(map(int, input().split()))
    ans = []
    for i in range(N-1, -1, -1):
        if a[i] == 0:
            continue
        ans.append(i+1)
        for j in range(2*i+1, N, i+1):
            a[j] = 1 - a[j]
    print(len(ans))
    print(*ans, sep=' ')
