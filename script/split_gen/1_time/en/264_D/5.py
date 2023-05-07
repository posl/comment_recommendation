def main():
    S = input()
    atcoder = "atcoder"
    ans = 0
    for i in range(len(S)):
        if S[i] == atcoder[i]:
            pass
        else:
            ans += 1
    print(ans)
