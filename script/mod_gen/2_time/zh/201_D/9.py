def main():
    s = input()
    count = 0
    for i in range(10000):
        if i < 1000:
            i = '0' * (4 - len(str(i))) + str(i)
        else:
            i = str(i)
        flag = True
        for j in range(10):
            if s[j] == 'o':
                if str(j) not in i:
                    flag = False
                    break
            elif s[j] == 'x':
                if str(j) in i:
                    flag = False
                    break
        if flag:
            count += 1
    print(count)

if __name__ == '__main__':
    main()