def solve():
    s = input()
    if len(s) == 1:
        if s == "8":
            print("Yes")
        else:
            print("No")
        return
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[1] + s[0]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        return
    count = [0] * 10
    for i in range(len(s)):
        count[int(s[i])] += 1
    for i in range(112, 1000, 8):
        c = [0] * 10
        c[int(str(i)[0])] += 1
        c[int(str(i)[1])] += 1
        c[int(str(i)[2])] += 1
        flag = True
        for j in range(10):
            if c[j] > count[j]:
                flag = False
                break
        if flag:
            print("Yes")
            return
    print("No")

if __name__ == '__main__':
    solve()