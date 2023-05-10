def main():
    # input
    S_1 = input()
    S_2 = input()
    S_3 = input()
    T = input()
    # solve
    ans = ""
    for i in range(len(T)):
        if T[i] == "1":
            ans += S_1
        elif T[i] == "2":
            ans += S_2
        else:
            ans += S_3
    # output
    print(ans)
