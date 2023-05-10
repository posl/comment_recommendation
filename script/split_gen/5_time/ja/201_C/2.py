def main():
    s = input()
    cnt = 0
    for i in range(10000):
        tmp = str(i).zfill(4)
        flag = True
        for j in range(10):
            if s[j] == "o" and tmp.count(str(j)) == 0:
                flag = False
            if s[j] == "x" and tmp.count(str(j)) > 0:
                flag = False
        if flag:
            cnt += 1
    print(cnt)
