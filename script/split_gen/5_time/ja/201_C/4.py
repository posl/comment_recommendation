def main():
    s = input()
    cnt = 0
    for i in range(10000):
        num = str(i).zfill(4)
        for j in range(10):
            if s[j] == 'o' and str(j) not in num:
                break
            if s[j] == 'x' and str(j) in num:
                break
        else:
            cnt += 1
    print(cnt)
