def main():
    # input
    s = input()
    # count
    count = 0
    # loop
    for i in range(10000):
        # change to string
        i = str(i).zfill(4)
        # flag
        flag = True
        # loop
        for j in range(10):
            # if s[j] is o
            if s[j] == 'o':
                # if j is not in i
                if str(j) not in i:
                    # flag is False
                    flag = False
                    # break
                    break
            # if s[j] is x
            elif s[j] == 'x':
                # if j is in i
                if str(j) in i:
                    # flag is False
                    flag = False
                    # break
                    break
        # if flag is True
        if flag:
            # count + 1
            count += 1
    # print(count)
    print(count)
main()
