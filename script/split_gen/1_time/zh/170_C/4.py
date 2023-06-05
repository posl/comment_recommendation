def find_closest_num(array, num):
    if len(array) == 0:
        return num
    else:
        closest_num = array[0]
        for n in array:
            if abs(num-n) < abs(num-closest_num):
                closest_num = n
        return closest_num
input_str = input()
input_list = input_str.split()
x = int(input_list[0])
n = int(input_list[1])
