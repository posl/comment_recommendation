def problem201_c():
    s = input()
    count = 0
    for i in range(10000):
        num = str(i).zfill(4)
        for j in range(10):
            if s[j] == 'o' and str(j) not in num:
                break
            elif s[j] == 'x' and str(j) in num:
                break
        else:
            count += 1
    print(count)
