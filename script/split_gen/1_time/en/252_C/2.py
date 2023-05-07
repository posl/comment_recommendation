def main():
    N = int(input())
    S = []
    for i in range(N):
        S.append(input())
    ans = 0
    for i in range(10):
        num = 0
        for j in range(N):
            num = max(num, S[j].count(str(i)))
        ans += num
    print(ans)
