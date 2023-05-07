def main():
    S = input()
    N = len(S)
    ans = [0] * N
    for i in range(N):
        if S[i] == "R":
            ans[i + 1] += 1
        else:
            ans[i - 1] += 1
    for i in range(N):
        if ans[i] % 2 == 1:
            if S[i] == "R":
                ans[i + 1] += 1
            else:
                ans[i - 1] += 1
    for i in range(N):
        print(ans[i] // 2, end = " ")
    print()
