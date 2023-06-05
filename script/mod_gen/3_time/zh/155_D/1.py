def get_input():
    input_str = input()
    input_list = input_str.split()
    n = int(input_list[0])
    k = int(input_list[1])
    input_str = input()
    input_list = input_str.split()
    a_list = []
    for i in range(n):
        a_list.append(int(input_list[i]))
    return n, k, a_list

if __name__ == '__main__':
    get_input()