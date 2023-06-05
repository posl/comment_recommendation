def main():
    N = int(input())
    count = 0
    for i in range(1,N+1):
        if i%10 == 0:
            continue
        else:
            str_i = str(i)
            len_i = len(str_i)
            if str_i[-1] == str_i[0]:
                count += 1
            else:
                if len_i == 1:
                    continue
                else:
                    for j in range(1,len_i):
                        if str_i[j] == str_i[j-1]:
                            count += 1
                            break
    print(count)
main()
