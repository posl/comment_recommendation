def main():
    S = input()
    ans = 0
    for i in range(10000):
        pin = str(i).zfill(4)
        for j in range(4):
            if S[j] == "o" and pin[j] != "0":
                break
            if S[j] == "x" and pin[j] == "0":
                break
        else:
            for j in range(4):
                if S[j+4] == "o" and pin[j] != "1":
                    break
                if S[j+4] == "x" and pin[j] == "1":
                    break
            else:
                ans += 1
    print(ans)
main()
