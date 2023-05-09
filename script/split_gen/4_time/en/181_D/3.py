def main():
    s = input()
    n = len(s)
    if n == 1:
        if int(s) == 8:
            print("Yes")
        else:
            print("No")
    elif n == 2:
        if int(s) % 8 == 0 or int(s[::-1]) % 8 == 0:
            print("Yes")
        else:
            print("No")
    else:
        cnt = [0] * 10
        for i in range(n):
            cnt[int(s[i])] += 1
        for i in range(112, 1000, 8):
            c = [0] * 10
            for j in range(3):
                c[int(str(i)[j])] += 1
            ok = True
            for j in range(10):
                if cnt[j] < c[j]:
                    ok = False
            if ok:
                print("Yes")
                exit()
        print("No")
