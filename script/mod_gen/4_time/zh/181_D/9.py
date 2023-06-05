def main():
    s = input()
    if len(s) == 1:
        if s == "8":
            print("是")
        else:
            print("否")
        return
    if len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print("是")
        else:
            print("否")
        return
    # 3位以上的数字
    num_dict = {}
    for i in range(10):
        num_dict[i] = 0
    for i in range(len(s)):
        num_dict[int(s[i])] += 1
    # 3位数的情况
    for i in range(112, 1000, 8):
        if i % 8 == 0:
            tmp_dict = num_dict.copy()
            tmp = str(i)
            flag = True
            for j in range(len(tmp)):
                if tmp_dict[int(tmp[j])] > 0:
                    tmp_dict[int(tmp[j])] -= 1
                else:
                    flag = False
                    break
            if flag:
                print("是")
                return
    print("否")

if __name__ == '__main__':
    main()