def main():
    S = input()
    T = input()
    ans = "No"
    for i in range(len(S)):
        if S == T:
            ans = "Yes"
            break
        S = S[1:] + S[0]
    print(ans)
