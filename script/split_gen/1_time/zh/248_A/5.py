def get_missing_number(input):
    input_list = list(input)
    input_list.sort()
    for i in range(0, 9):
        if input_list[i] != str(i):
            return i
input = input()
print(get_missing_number(input))
