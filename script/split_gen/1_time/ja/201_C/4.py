def main():
    s = input()
    ans = 0
    for i in range(10000):
        flag = True
        for j in range(10):
            if s[j] == "o" and str(i).find(str(j)) == -1:
                flag = False
            if s[j] == "x" and str(i).find(str(j)) != -1:
                flag = False
        if flag:
            ans += 1
    print(ans)
