def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    cnt = [0] * 10
    for i in a:
        cnt[i] += 1
    ans = [0] * 10
    for i in range(10):
        ans[i] = (cnt[i] * (cnt[i] - 1)) // 2
    for i in range(10):
        for j in range(i + 1, 10):
            ans[(i * j) % 10] += cnt[i] * cnt[j]
    for i in ans:
        print(i)
