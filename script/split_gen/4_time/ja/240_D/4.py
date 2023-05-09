def main():
    n = int(input())
    a = list(map(int, input().split()))
    ball = [0] * (2 * 10 ** 5 + 1)
    ans = []
    for i in range(n):
        ball[a[i]] += 1
        if ball[a[i]] == 2:
            ball[a[i]] = 0
        ans.append(sum(ball))
    print(*ans, sep="\n")
