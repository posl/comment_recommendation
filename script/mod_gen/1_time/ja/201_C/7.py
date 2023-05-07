def main():
    S = input()
    S_list = list(S)
    count = 0
    for i in range(10000):
        i = str(i).zfill(4)
        i_list = list(i)
        flag = True
        for j in range(10):
            if S_list[j] == 'o':
                if str(j) not in i_list:
                    flag = False
                    break
            elif S_list[j] == 'x':
                if str(j) in i_list:
                    flag = False
                    break
        if flag:
            count += 1
    print(count)

if __name__ == '__main__':
    main()