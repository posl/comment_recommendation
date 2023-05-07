def main():
    S = input()
    ans = ""
    for i in range(3):
        ans += str(int(S[i]))
    ans += "0"
    print(ans)
main()
