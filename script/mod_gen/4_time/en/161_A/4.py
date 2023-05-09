def main():
    input_string = input()
    input_list = input_string.split()
    box_a = int(input_list[0])
    box_b = int(input_list[1])
    box_c = int(input_list[2])
    box_a, box_b = box_b, box_a
    box_a, box_c = box_c, box_a
    print(str(box_a) + " " + str(box_b) + " " + str(box_c))

if __name__ == '__main__':
    main()