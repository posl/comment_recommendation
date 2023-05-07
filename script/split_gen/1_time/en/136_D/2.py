def main():
    S = input()
    N = len(S)
    ans = [0] * N
    ans[0] = 1
    ans[-1] = 1
    i = 0
    while i < N - 1:
        if S[i] == 'R' and S[i + 1] == 'L':
            j = i + 1
            while j < N - 1 and S[j] == 'L' and S[j + 1] == 'L':
                j += 1
            ans[i] = ans[i] + (j - i + 1) // 2
            ans[i + 1] = ans[i + 1] + (j - i + 1) // 2
            if (j - i + 1) % 2 == 1:
                ans[i + 1] += 1
            i = j
        else:
            i += 1
    i = N - 1
    while i > 0:
        if S[i] == 'L' and S[i - 1] == 'R':
            j = i - 1
            while j > 0 and S[j] == 'R' and S[j - 1] == 'R':
                j -= 1
            ans[i] = ans[i] + (i - j + 1) // 2
            ans[i - 1] = ans[i - 1] + (i - j + 1) // 2
            if (i - j + 1) % 2 == 1:
                ans[i - 1] += 1
            i = j
        else:
            i -= 1
    print(*ans)
