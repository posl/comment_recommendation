def main():
    N = int(input())
    str_list = []
    for i in range(N):
        str_list.append(input())
    for i in range(N):
        if str_list.count(str_list[i]) > 1:
            print(str_list[i] + "(" + str(str_list.count(str_list[i])-1) + ")")
        else:
            print(str_list[i])

if __name__ == '__main__':
    main()