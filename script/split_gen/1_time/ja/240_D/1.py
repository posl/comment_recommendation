def main():
    N = int(input())
    a = list(map(int, input().split()))
    cnt = [0] * (2 * 10 ** 5 + 1)
    for i in range(N):
        cnt[a[i]] += 1
        if cnt[a[i]] == a[i]:
            print(i + 1)
            return
        else:
            print(i + 1 - cnt[a[i]] + 1)
