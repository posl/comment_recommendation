def main():
    S = input()
    ans = ""
    for i in range(3):
        if S[i] == "1":
            ans += "1"
        else:
            ans += "0"
    if S[3] == "1":
        ans += "0"
    else:
        ans += "0"
    print(ans)
