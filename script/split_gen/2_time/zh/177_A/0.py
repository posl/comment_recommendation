def main():
    #input
    input_line = input()
    input_list = input_line.split(' ')
    D = int(input_list[0])
    T = int(input_list[1])
    S = int(input_list[2])
    #calc
    if D <= T * S:
        print('Yes')
    else:
        print('No')
