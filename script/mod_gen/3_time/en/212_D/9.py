def main():
    Q = int(input())
    sum = 0
    min = 10**9
    min_list = []
    for i in range(Q):
        input_list = input().split()
        if input_list[0] == '1':
            sum += int(input_list[1])
        elif input_list[0] == '2':
            sum += int(input_list[1])
            min += int(input_list[1])
        else:
            min_list.append(min)
            min = 10**9
    for i in min_list:
        print(i+sum)

if __name__ == '__main__':
    main()