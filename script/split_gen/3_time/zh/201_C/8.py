def problem201_c():
    s = input()
    #print(s)
    count = 0
    for i in range(10000):
        #print(i)
        i = str(i).zfill(4)
        #print(i)
        flag = True
        for j in range(10):
            #print(j)
            if s[j] == 'o' and str(j) not in i:
                flag = False
                break
            elif s[j] == 'x' and str(j) in i:
                flag = False
                break
        if flag:
            #print(i)
            count += 1
    print(count)
