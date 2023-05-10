def main():
    input_str = input()
    input_list = list(input_str)
    if (input_list[0] == input_list[1] and input_list[1] == input_list[2] and input_list[2] == input_list[3]):
        print("Weak")
    else:
        weak = False
        for i in range(0, 3):
            if (int(input_list[i]) != 9):
                if (int(input_list[i]) + 1 != int(input_list[i + 1])):
                    weak = True
                    break
            else:
                if (int(input_list[i + 1]) != 0):
                    weak = True
                    break
        if (weak):
            print("Strong")
        else:
            print("Weak")

if __name__ == '__main__':
    main()