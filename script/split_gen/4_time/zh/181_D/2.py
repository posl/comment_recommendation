def main():
    input_str = input()
    input_list = list(input_str)
    input_list = [int(x) for x in input_list]
    input_list.sort()
    input_list.reverse()
    input_str = "".join(str(x) for x in input_list)
    #print(input_list)
    #print(input_str)
    if int(input_str) % 8 == 0:
        print("是")
    else:
        print("否")
