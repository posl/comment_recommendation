def main():
    s = input()
    if len(s) == 1:
        if s == "8":
            print("Yes")
        else:
            print("No")
        return
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        return
    count = [0] * 10
    for i in range(len(s)):
        count[int(s[i])] += 1
    for i in range(112, 1000, 8):
        tmp = [0] * 10
        tmp[i % 10] += 1
        tmp[(i % 100) // 10] += 1
        tmp[i // 100] += 1
        flag = True
        for j in range(10):
            if tmp[j] > count[j]:
                flag = False
                break
        if flag:
            print("Yes")
            return
    print("No")
    return

if __name__ == '__main__':
    main()