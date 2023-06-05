def main():
    s = input()
    cnt = 0
    for i in range(10000):
        pin = "{:0>4}".format(i)
        flag = True
        for j in range(10):
            if s[j] == 'o' and str(j) not in pin:
                flag = False
                break
            if s[j] == 'x' and str(j) in pin:
                flag = False
                break
        if flag:
            cnt += 1
    print(cnt)
