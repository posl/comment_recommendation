def solve():
    s = input()
    if len(s) == 1:
        if s == "8":
            print("Yes")
        else:
            print("No")
        return
    elif len(s) == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
        return
    else:
        cnt = [0] * 10
        for i in s:
            cnt[int(i)] += 1
        for i in range(112, 1000, 8):
            tmp = [0] * 10
            for j in str(i):
                tmp[int(j)] += 1
            flag = True
            for j in range(10):
                if tmp[j] > cnt[j]:
                    flag = False
                    break
            if flag:
                print("Yes")
                return
        print("No")
        return
