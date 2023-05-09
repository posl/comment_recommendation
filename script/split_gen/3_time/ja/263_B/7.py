def main():
    n = int(input())
    p = list(map(int, input().split()))
    ans = [0] * n
    for i in range(n):
        ans[i] = 1
        j = p[i]
        while j > 0:
            ans[i] += 1
            j = p[j - 1]
    print(max(ans))
