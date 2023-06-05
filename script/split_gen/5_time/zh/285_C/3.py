def main():
    S = input()
    ans = 0
    for i in range(len(S)):
        ans = ans * 26 + ord(S[i]) - ord('A') + 1
    print(ans)
