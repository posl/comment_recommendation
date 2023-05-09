def main():
    S = input()
    ans = 0
    for i in range(3):
        if S[i] == "a":
            ans += 1
        elif S[i] == "b":
            ans += 2
        else:
            ans += 3
    print(ans)
