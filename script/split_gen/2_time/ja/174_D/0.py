def main():
    N = int(input())
    S = input()
    ans = 0
    for i in range(N):
        if i % 2 == 0:
            if S[i] == "W":
                ans += 1
        else:
            if S[i] == "R":
                ans += 1
    print(min(ans, N - ans))
