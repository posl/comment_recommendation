def main():
    input_line = input()
    input_list = input_line.split()
    input_list = list(map(int, input_list))
    input_list.sort()
    distinct_count = 1
    for i in range(len(input_list)-1):
        if input_list[i] != input_list[i+1]:
            distinct_count += 1
    print(distinct_count)
