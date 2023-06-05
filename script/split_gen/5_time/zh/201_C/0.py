def main():
    s = input()
    count = 0
    for i in range(0, 10000):
        str_i = str(i).zfill(4)
        flag = True
        for j in range(0, 10):
            if s[j] == 'o':
                if str_i.find(str(j)) == -1:
                    flag = False
                    break
            elif s[j] == 'x':
                if str_i.find(str(j)) != -1:
                    flag = False
                    break
        if flag:
            count += 1
    print(count)
