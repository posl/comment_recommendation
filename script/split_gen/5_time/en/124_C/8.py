def main():
    input_str = input()
    input_list = list(input_str)
    #print(input_list)
    count = 0
    for i in range(len(input_list)-1):
        if input_list[i] == input_list[i+1]:
            count += 1
    print(count)
