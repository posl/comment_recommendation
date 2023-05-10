def check(s):
    for i in range(len(s)-5):
        if s[i:i+6] == "......":
            return True
    return False
n = int(input())
s = [input() for _ in range(n)]
for i in range(n):
    for j in range(n):
        if s[i][j] == ".":
            s[i] = s[i][:j] + "#" + s[i][j+1:]
            if check(s[i]):
                print("Yes")
                exit()
            s[i] = s[i][:j] + "." + s[i][j+1:]
        if s[j][i] == ".":
            s[j] = s[j][:i] + "#" + s[j][i+1:]
            if check(s[j]):
                print("Yes")
                exit()
            s[j] = s[j][:i] + "." + s[j][i+1:]
print("No")

if __name__ == '__main__':
    check()