def main():
    S = input()
    ans = 0
    count = 0
    for i in range(len(S)):
        if S[i] == "A" or S[i] == "C" or S[i] == "G" or S[i] == "T":
            count += 1
        else:
            ans = max(ans, count)
            count = 0
    ans = max(ans, count)
    print(ans)
