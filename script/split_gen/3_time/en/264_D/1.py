def main():
    S = input()
    T = "atcoder"
    ans = 0
    for i in range(len(S)):
        if S[i] != T[i]:
            ans += abs(ord(S[i]) - ord(T[i]))
    print(ans)
