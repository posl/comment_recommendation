def main():
    input_str = input()
    input_list = input_str.split()
    input_list = [int(x) for x in input_list]
    input_list.sort()
    if input_list[0] == input_list[1] and input_list[1] == input_list[2] and input_list[3] == input_list[4]:
        print("Yes")
    elif input_list[0] == input_list[1] and input_list[2] == input_list[3] and input_list[3] == input_list[4]:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()