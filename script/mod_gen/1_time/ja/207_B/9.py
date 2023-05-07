def get_input_lines_int_array():
    return list(map(int, input().split()))
A, B, C, D = get_input_lines_int_array()
count = 0
while A > C * D:
    count += 1
    A += B
    C += D

if __name__ == '__main__':
    get_input_lines_int_array()