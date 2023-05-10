def solve():
    S = input()
    ans = 0
    for i in range(len(S)):
        if S[i] == "w":
            ans += i
    print(ans)
