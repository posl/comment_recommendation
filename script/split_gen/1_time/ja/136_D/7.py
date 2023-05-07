def main():
    S = input()
    N = len(S)
    ans = [0] * N
    i = 0
    while i < N:
        if S[i] == "R":
            j = i
            while j < N and S[j] == "R":
                j += 1
            if j - i == 1:
                ans[i] = 1
                i += 1
            else:
                ans[j-1] = (j - i) // 2
                ans[j] = (j - i) - ans[j-1]
                i = j + 1
        else:
            j = i
            while j < N and S[j] == "L":
                j += 1
            if j - i == 1:
                ans[i] = 1
                i += 1
            else:
                ans[i-1] = (j - i) // 2
                ans[i] = (j - i) - ans[i-1]
                i = j + 1
    print(*ans)
