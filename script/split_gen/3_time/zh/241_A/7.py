def main():
    input_str = input()
    input_list = input_str.split()
    input_list = list(map(int, input_list))
    count = 0
    while count < 3:
        input_list = list(map(lambda x:input_list[x], input_list))
        count += 1
    print(input_list[0])
