def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == "0":
            continue
        else:
            ans += 1
            if i != len(S) - 1:
                ans += 1
    print(ans)
