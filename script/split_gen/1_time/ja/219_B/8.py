def main():
    S_1 = input()
    S_2 = input()
    S_3 = input()
    T = input()
    ans = ""
    for i in T:
        if i == "1":
            ans += S_1
        elif i == "2":
            ans += S_2
        else:
            ans += S_3
    print(ans)
