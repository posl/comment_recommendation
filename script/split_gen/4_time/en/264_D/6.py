def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] != "atcoder"[i]:
            ans += 1
    print(ans)
