def main():
    s = input()
    cnt = 0
    for i in range(10000):
        i = str(i).zfill(4)
        flag = True
        for j in range(10):
            if s[j] == 'o' and str(j) not in i:
                flag = False
            elif s[j] == 'x' and str(j) in i:
                flag = False
        if flag:
            cnt += 1
    print(cnt)
