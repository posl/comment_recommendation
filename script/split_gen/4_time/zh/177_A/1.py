def main():
    input_str = input()
    input_list = input_str.split()
    D = int(input_list[0])
    T = int(input_list[1])
    S = int(input_list[2])
    if D % S == 0:
        if D / S <= T:
            print('Yes')
        else:
            print('No')
    else:
        if D / S + 1 <= T:
            print('Yes')
        else:
            print('No')
