def main():
    S = input()
    ans = ""
    for i in range(4):
        if S[i] == "1":
            ans = ans + "0"
        else:
            ans = ans + S[i]
    print(ans)
