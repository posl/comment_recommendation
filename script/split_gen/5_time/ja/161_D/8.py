def main():
    k = int(input())
    count = 0
    i = 0
    while count < k:
        i += 1
        if i < 10:
            count += 1
        else:
            s = str(i)
            flag = True
            for j in range(len(s) - 1):
                if abs(int(s[j]) - int(s[j + 1])) > 1:
                    flag = False
                    break
            if flag:
                count += 1
    print(i)
