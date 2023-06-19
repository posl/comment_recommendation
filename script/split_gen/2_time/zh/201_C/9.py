def main():
    s = list(input())
    count = 0
    for i in range(10000):
        i = str(i).zfill(4)
        flag = True
        for j in range(10):
            if s[j] == 'o' and str(j) not in i:
                flag = False
                break
            if s[j] == 'x' and str(j) in i:
                flag = False
                break
        if flag:
            count += 1
    print(count)
