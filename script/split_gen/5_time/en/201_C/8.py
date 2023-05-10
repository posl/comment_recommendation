def main():
    s = input()
    count = 0
    for i in range(10000):
        if len(str(i)) < 4:
            i = str(i).zfill(4)
        else:
            i = str(i)
        flag = True
        for j in range(len(s)):
            if s[j] == 'o' and str(j) not in i:
                flag = False
                break
            if s[j] == 'x' and str(j) in i:
                flag = False
                break
        if flag:
            count += 1
    print(count)
