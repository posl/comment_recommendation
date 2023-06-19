def main():
    input_str = input()
    input_list = input_str.split()
    input_list = list(map(int, input_list))
    input_list = set(input_list)
    print(len(input_list))

if __name__ == '__main__':
    main()