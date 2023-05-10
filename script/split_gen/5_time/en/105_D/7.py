def get_input():
    input_line = input()
    input_line = input_line.split()
    num_boxes = int(input_line[0])
    num_children = int(input_line[1])
    input_line = input()
    input_line = input_line.split()
    candies = [int(i) for i in input_line]
    return num_boxes, num_children, candies
