def main():
    n = int(input())
    s = []
    for i in range(n):
        s.append(input())
    ans = [0] * n
    for i in range(n):
        for j in range(i):
            if s[i] == s[j]:
                ans[i] = ans[j] + 1
                break
    for i in range(n):
        if ans[i] == 0:
            print(s[i])
        else:
            print(s[i] + "(" + str(ans[i]) + ")")
