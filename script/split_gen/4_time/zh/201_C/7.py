def main():
    s = input()
    count = 0
    for i in range(10000):
        pin = "{:04d}".format(i)
        flg = True
        for j in range(10):
            if s[j] == 'o' and str(j) not in pin:
                flg = False
            if s[j] == 'x' and str(j) in pin:
                flg = False
        if flg:
            count += 1
    print(count)
