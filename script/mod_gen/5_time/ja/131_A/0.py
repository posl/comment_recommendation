def check_same_number(input_str):
    if input_str[0] == input_str[1]:
        if input_str[0] == input_str[2]:
            return True
    if input_str[1] == input_str[2]:
        if input_str[1] == input_str[3]:
            return True
    return False
input_str = input()

if __name__ == '__main__':
    check_same_number()