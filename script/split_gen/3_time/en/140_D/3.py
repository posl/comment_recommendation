def main():
    n, k = map(int, input().split())
    s = input()
    if s.count("L") == 0 or s.count("R") == 0:
        print(n - 1)
        return
    if s[0] == "R":
        s = "L" + s
    if s[-1] == "L":
        s = s + "R"
    s = s.replace("LR", "L R")
    s = s.replace("RL", "R L")
    s = s.split()
    for i in range(len(s)):
        if s[i][0] == "R":
            s[i] = s[i][1:]
        if s[i][-1] == "L":
            s[i] = s[i][:-1]
    s = [i for i in s if len(i) > 0]
    if len(s) <= k:
        print(n)
        return
    ans = 0
    for i in range(k + 1):
        ans += len(s[i])
    print(ans)
main()
