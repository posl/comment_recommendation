def main():
    input_str = input()
    input_list = list(input_str)
    input_list = list(map(int, input_list))
    input_list.sort()
    for i in range(10):
        if i not in input_list:
            print(i)
            break

if __name__ == '__main__':
    main()