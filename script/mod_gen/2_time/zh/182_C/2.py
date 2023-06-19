def main():
    n = input()
    n = int(n)
    n_list = list(str(n))
    n_list.reverse()
    #print(n_list)
    n_len = len(n_list)
    k = 0
    for i in range(n_len):
        if n_list[i] == '0':
            k += 1
        else:
            break
    #print(k)
    if k == n_len:
        print(-1)
    else:
        #print(n_list[k:])
        #print(len(n_list[k:]))
        sum = 0
        for i in range(len(n_list[k:])):
            sum += int(n_list[k+i])
        #print(sum)
        if sum % 3 == 0:
            print(k)
        else:
            print(-1)

if __name__ == '__main__':
    main()