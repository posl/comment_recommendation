def main():
    N = int(input())
    S = input()
    ans = ""
    for i in range(len(S)):
        if S[i] == "Z":
            ans += "A"
        else:
            ans += chr(ord(S[i])+N)
    print(ans)
